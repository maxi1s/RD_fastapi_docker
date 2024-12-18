from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProviderAddCreateUpdateSchema(BaseModel):
    provider_add_id: Optional[int] = None  # Идентификатор записи, может быть None, так как SERIAL автоинкрементируется
    provider_add_stack: Optional[int] = None
    provider_add_date: Optional[date] = None
    additional_product_id: Optional[int] = None
    provider_id: Optional[int] = None

    class Config:
        orm_mode = True  # Включает поддержку работы с ORM объектами