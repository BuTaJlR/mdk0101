from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = None

class User(BaseModelModify):
    login: str
    password: str

class Personal(User):
    power_level: int = 1

class Ticket(BaseModelModify):
    excursionId: int
    userId: int
    price: int

class Excursion(BaseModelModify):
    presonalId: int
    museumId: int


class Museum(BaseModelModify):
    name: str


