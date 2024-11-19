from pydantic import BaseModel

class FlowerCreateSchema(BaseModel):
    name: str
    lifespan: int
    stock: int
    provider_flower_id: int
#нужен фикс.
class FlowerSchema(FlowerCreateSchema):
    id: int

    class Config:
        orm_mode = True