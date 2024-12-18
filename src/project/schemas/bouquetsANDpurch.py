from pydantic import BaseModel
from typing import Optional

class BouquetsCreateUpdateSchema(BaseModel):
    bouquets_id: Optional[int] = None
    bouquet_name: Optional[str] = None
    bouquet_life_span: Optional[int] = None
    bouquet_info: Optional[str] = None
    bouquet_stock: Optional[int] = None
    bouquet_price: Optional[float] = None

    class Config:
        orm_mode = True

class BouquetsPurchaseCreateUpdateSchema(BaseModel):
    bouquets_purchase_id: Optional[int] = None
    check_id: Optional[int] = None
    bouquet_id: Optional[int] = None
    bouquet_quantity: Optional[int] = None
    bouquets_price: Optional[float] = None

    class Config:
        orm_mode = True