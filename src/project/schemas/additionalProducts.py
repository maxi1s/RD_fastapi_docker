from pydantic import BaseModel
from typing import Optional

class AdditionalProductsCreateUpdateSchema(BaseModel):
    additional_products_id: Optional[int] = None
    additional_product_name: Optional[str] = None
    additional_product_stock: Optional[int] = None
    provider_add_id: Optional[int] = None

    class Config:
        orm_mode = True