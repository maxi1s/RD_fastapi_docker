from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProviderFlowerCreateUpdateSchema(BaseModel):
    providers_flower_stack: Optional[int] = None  # Количество цветов на складе, может быть None
    providers_flower_date: Optional[date] = None  # Дата поставки цветов, может быть None
    providers_flower_flower_id: Optional[int] = None  # Идентификатор цветка, может быть None
    provider_id: Optional[int] = None  # Внешний ключ, ссылающийся на таблицу Provider, может быть None

    class Config:
        orm_mode = True  # Включает поддержку работы с ORM объектами