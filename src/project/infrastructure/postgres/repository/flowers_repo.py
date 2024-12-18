from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from project.infrastructure.postgres.models import Flowers
from project.schemas.flowers import FlowerCreateUpdateSchema
from project.core.exceptions import FlowerNotFound, FlowerAlreadyExists

class FlowerRepository:
    async def get_flowers(self, session: AsyncSession):
        result = await session.execute(select(Flowers))
        flowers = result.scalars().all()
        return [FlowerSchema.from_orm(flower) for flower in flowers]

    async def get_flower_by_name(self, session: AsyncSession, name: str):
        result = await session.execute(select(Flowers).where(Flowers.name == name))
        flower = result.scalar_one_or_none()
        if flower is None:
            raise FlowerNotFound(name=name)
        return FlowerSchema.from_orm(flower)

    async def get_flower_by_id(self, session: AsyncSession, flower_id: int):
        result = await session.execute(select(Flowers).where(Flowers.id == flower_id))
        flower = result.scalar_one_or_none()
        if flower is None:
            raise FlowerNotFound(_id=flower_id)
        return FlowerSchema.from_orm(flower)

    async def create_flower(self, session: AsyncSession, flower_data: FlowerCreateSchema) -> FlowerSchema:
        existing_flower = await session.execute(
            select(Flowers).where(Flowers.name == flower_data.name)
        )
        if existing_flower.scalar_one_or_none():
            raise FlowerAlreadyExists(name=flower_data.name)

        new_flower = Flowers(**flower_data.dict())
        session.add(new_flower)
        await session.commit()
        await session.refresh(new_flower)
        return FlowerSchema.from_orm(new_flower)

    async def update_flower(self, session: AsyncSession, flower_id: int, flower_data: FlowerCreateSchema):
        result = await session.execute(select(Flowers).where(Flowers.id == flower_id))
        flower = result.scalar_one_or_none()
        if flower is None:
            raise FlowerNotFound(_id=flower_id)

        for key, value in flower_data.dict().items():
            setattr(flower, key, value)

        try:
            await session.commit()
            await session.refresh(flower)
        except IntegrityError:
            await session.rollback()
            raise FlowerAlreadyExists(name=flower_data.name)

        return FlowerSchema.from_orm(flower)

    async def delete_flower(self, session: AsyncSession, flower_id: int):
        result = await session.execute(select(Flowers).where(Flowers.id == flower_id))
        flower = result.scalar_one_or_none()
        if flower is None:
            raise FlowerNotFound(_id=flower_id)

        await session.delete(flower)
        await session.commit()