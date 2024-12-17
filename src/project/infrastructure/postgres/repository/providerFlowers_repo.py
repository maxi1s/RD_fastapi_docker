from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from project.infrastructure.postgres.models import ProviderFlowers
from project.schemas.providerFlowers import ProviderFlowerCreateSchema, ProviderFlowerSchema
from project.core.exceptions import ProviderAlreadyExists

class providerFlowersRepository:
    async def get_all_providers(self, session: AsyncSession):
        result = await session.execute(select(ProviderFlowers))
        providers = result.scalars().all()
        return [ProviderFlowerSchema.from_orm(providers) for providers in providers]

    async def create_provider(self, session: AsyncSession, provider_data: ProviderFlowerCreateSchema) -> ProviderFlowerSchema:
        existing_provider = await session.execute(
            select(ProviderFlowers).where(ProviderFlowers.name == provider_data.name)
        )
        if existing_provider.scalar_one_or_none():
            raise ProviderAlreadyExists(f"Поставщик с именем '{provider_data.name}' уже существует")

        new_provider = ProviderFlowers(**provider_data.dict())
        session.add(new_provider)
        await session.commit()
        await session.refresh(new_provider)
        return ProviderFlowerSchema.from_orm(new_provider)
