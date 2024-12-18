from pydantic import BaseModel
from typing import Optional

class CustomerCreateSchema(BaseModel):
    customer_id: Optional[int] = None  # Идентификатор клиента, может быть None
    customer_name: str  # Имя клиента
    customer_adres: str  # Адрес клиента
    customer_summ: float  # Сумма клиента
    customer_phone: str  # Телефон клиента

    class Config:
        orm_mode = True