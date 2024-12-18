from pydantic import BaseModel
from typing import Optional

class FlowerCreateUpdateSchema(BaseModel):
    flowers_id: Optional[int] = None
    flowers_name: Optional[str] = None
    flower_life_span: Optional[int] = None
    flower_stock: Optional[int] = None
    provider_flower_id: Optional[int] = None
    flower_price: Optional[float] = None

    class Config:
        orm_mode = True