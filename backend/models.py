import datetime
from sqlmodel import SQLModel, Field
from typing import Optional


class Coupon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    used: bool

class Action(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str = Field(nullable=False)
    name: str = Field(nullable=False)
    description: str = Field(nullable=True)
    # valid_until: datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
    discount_percent: int = Field(nullable=True)
    discount_value_currency: str = Field(nullable=True)
    discount_value: int = Field(nullable=True)



