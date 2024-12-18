from pydantic import BaseModel
from typing import Optional

class FlowersPurchaseCreateUpdateSchema(BaseModel):
    flowers_purchase_id: Optional[int] = None  # Идентификатор покупки цветов, может быть None, так как SERIAL автоинкрементируется
    check_id: Optional[int] = None  # Внешний ключ, ссылающийся на таблицу TotalChecks, может быть None
    flower_id: Optional[int] = None  # Внешний ключ, ссылающийся на таблицу Flowers, может быть None
    flower_quantity: Optional[int] = None  # Количество цветов, может быть None
    flowers_price: Optional[float] = None  # Цена цветов, может быть None

    class Config:
        orm_mode = True  # Включает поддержку работы с ORM объектами