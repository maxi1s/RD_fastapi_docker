from pydantic import BaseModel
from datetime import date 

class ProviderFlowerCreateSchema(BaseModel):
    stock: int | None
    date: date
    flower_id: int
    provider_id: int 

class ProviderFlowerSchema(ProviderFlowerCreateSchema):
    provider_flowers_id: int

    class Config:
        orm_mode = True
        from_attributes = True