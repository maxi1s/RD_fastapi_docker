from pydantic import BaseModel
from typing import Optional

class FlowerCreateSchema(BaseModel):
    name: str
    lifespan: int
    stock: int
    provider_flower_id: int | None
    flower_price: float

class FlowerSchema(FlowerCreateSchema):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True  # атрибут позволяет использовать метод from orm - преобразование в pydantic модель