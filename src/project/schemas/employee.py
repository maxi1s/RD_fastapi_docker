from pydantic import BaseModel
from typing import Optional
from datetime import date

class EmployeeCreateSchema(BaseModel):
    employee_id: Optional[int]  # Поскольку SERIAL обычно автоинкрементируется, это поле может быть необязательным
    employee_name: str
    employee_position: str
    employee_salaries: float
    employee_stash: date

    class Config:
        orm_mode = True  # Включает совместимость с ORM, если это необходимо