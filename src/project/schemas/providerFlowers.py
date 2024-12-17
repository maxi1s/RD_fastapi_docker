from pydantic import BaseModel
from datetime import date 

class ProviderFlowerCreateSchema(BaseModel):
    stock: int | None
    date: date
    flower_id: int
    company_name: str 
    contact_info: str | None

class ProviderFlowerSchema(ProviderFlowerCreateSchema):
    ProviderFlowersID: int

    class Config:
        orm_mode = True
        from_attributes = True