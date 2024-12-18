from pydantic import BaseModel
from typing import Optional
from datetime import date

class TotalChecksCreateUpdateSchema(BaseModel):
    total_checks_id: Optional[int] = None
    cash_register_id: Optional[int] = None
    purchase_date: Optional[date] = None
    total_cost: Optional[float] = None
    employees_id: Optional[int] = None
    customers_id: Optional[int] = None

    class Config:
        orm_mode = True

class DeliveryChecksCreateUpdateSchema(BaseModel):
    total_checks_id: Optional[int] = None
    delivery_id: Optional[int] = None
    courier_id: Optional[int] = None
    customers_id: Optional[int] = None

    class Config:
        orm_mode = True