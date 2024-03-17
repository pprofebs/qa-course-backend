from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_customer: bool
    purchased_courses: List[int] = []
