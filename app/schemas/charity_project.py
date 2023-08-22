from datetime import datetime
from typing import Optional

from pydantic import (BaseModel, Extra, Field, NonNegativeInt, PositiveInt,
                      validator)

from app.core.constants import STR_FIELD_MAX_LENGTH, STR_FIELD_MIN_LENGTH


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(
        None, min_length=STR_FIELD_MIN_LENGTH, max_length=STR_FIELD_MAX_LENGTH)
    description: Optional[str] = Field(None, min_length=STR_FIELD_MIN_LENGTH)
    full_amount: Optional[PositiveInt]


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(
        ..., min_length=STR_FIELD_MIN_LENGTH, max_length=STR_FIELD_MAX_LENGTH)
    description: str = Field(..., min_length=STR_FIELD_MIN_LENGTH)
    full_amount: int = Field(..., gt=0)

    class Config:
        extra = Extra.forbid


class CharityProjectDB(CharityProjectBase):
    id: int
    close_date: Optional[datetime]
    create_date: datetime = Field(default_factory=datetime.now)
    invested_amount: Optional[NonNegativeInt]
    fully_invested: Optional[bool]

    class Config:
        orm_mode = True


class CharityProjectUpdate(CharityProjectBase):

    @validator('name', 'description')
    def name_cannot_be_null(cls, value):
        if not value:
            raise ValueError('Имя проекта и описание не может быть пустым!')
        return value

    class Config:
        extra = Extra.forbid
