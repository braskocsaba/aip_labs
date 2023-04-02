from sqlmodel import SQLModel, Field
from typing import Optional


class Coupon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str
    used: bool


