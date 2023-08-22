from datetime import datetime
from typing import List, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models import Donation, CharityProject


async def close_item(
        item: Union[Donation, CharityProject]
) -> Union[Donation, CharityProject]:
    item.invested_amount = item.full_amount
    item.fully_invested = True
    item.close_date = datetime.now()
    return item


async def invest_funds(
        obj_in: Union[Donation, CharityProject],
        db_model: Union[Donation, CharityProject],
        session: AsyncSession
):
    db_obj_all = await session.execute(select(db_model).where(
        db_model.fully_invested == 0
    ).order_by(db_model.create_date))
    db_obj_all: List[
        Union[Donation, CharityProject]] = db_obj_all.scalars().all()
    if not db_obj_all:
        return obj_in

    for db_obj in db_obj_all:
        if obj_in.fully_invested:
            break
        remaining_funds_in = obj_in.full_amount - obj_in.invested_amount
        remaining_funds_db = db_obj.full_amount - db_obj.invested_amount
        if remaining_funds_db < remaining_funds_in:
            obj_in.invested_amount += remaining_funds_db
            db_obj = await close_item(db_obj)
        elif remaining_funds_db == remaining_funds_in:
            obj_in = await close_item(obj_in)
            db_obj = await close_item(db_obj)
        else:
            obj_in = await close_item(obj_in)
            db_obj.invested_amount += remaining_funds_in
        session.add(obj_in)
        session.add(db_obj)

    await session.commit()
    await session.refresh(obj_in)
    return obj_in
