from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from project.infrastructure.postgres.models import ProviderFlowers
from project.schemas.providerFlowers import ProviderFlowerCreateSchema, ProviderFlowerSchema
from project.core.exceptions import ProviderAlreadyExists

class ProviderFlowersRepository:
    async def get_all_providers(self, session: AsyncSession):
        result = await session.execute(select(ProviderFlowers))
        providers = result.scalars().all()
        return [ProviderFlowerSchema.from_orm(provider) for provider in providers]

    async def create_provider(self, session: AsyncSession, provider_data: ProviderFlowerCreateSchema) -> ProviderFlowerSchema:
        existing_provider = await session.execute(
            select(ProviderFlowers).where(
                ProviderFlowers.provider_id == provider_data.provider_id,
                ProviderFlowers.flower_id == provider_data.flower_id
            )
        )
        if existing_provider.scalar_one_or_none():
            raise ProviderAlreadyExists(f"Поставщик с ID '{provider_data.provider_id}' и цветком ID '{provider_data.flower_id}' уже существует")

        new_provider = ProviderFlowers(**provider_data.dict())
        session.add(new_provider)
        await session.commit()
        await session.refresh(new_provider)
        return ProviderFlowerSchema.from_orm(new_provider)