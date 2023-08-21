from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, NonNegativeInt, PositiveInt


class DonationBase(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]


class DonationCreate(DonationBase):

    class Config:
        extra = Extra.forbid


class DonationDB(DonationBase):
    id: int
    user_id: int
    close_date: Optional[datetime]
    create_date: Optional[datetime] = Field(default_factory=datetime.now)
    invested_amount: Optional[NonNegativeInt] = Field(0)
    fully_invested: Optional[bool] = Field(False)

    class Config:
        orm_mode = True
