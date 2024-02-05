from datetime import datetime
from typing import List, Union

from pydantic import BaseModel, PositiveInt, Field, EmailStr


# создаём модель данных, которая обычно расположена в файле models.py
class User(BaseModel):
    id: int
    name: str


class Feedback(BaseModel):
    name: str
    message: str

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt
    is_subscribed: bool = False


