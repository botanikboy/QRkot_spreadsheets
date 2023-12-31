from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import CharityProject, User
from app.schemas.donation import DonationCreate, DonationDB
from app.services.investment import invest_funds

router = APIRouter()


@router.post(
    '/', response_model=DonationDB,
    response_model_exclude_none=True,
    response_model_exclude={
        'user_id',
        'close_date',
        'fully_invested',
        'invested_amount'
    }
)
async def create_new_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    new_donation = await donation_crud.create(
        donation, session, user)
    new_donation = await invest_funds(new_donation, CharityProject, session)
    return new_donation


@router.get('/',
            response_model=List[DonationDB],
            dependencies=[Depends(current_superuser)],
            response_model_exclude_none=True
            )
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    all_donations = await donation_crud.get_multi(session)
    return all_donations


@router.get(
    '/my',
    response_model=List[DonationDB],
    response_model_exclude={
        'user_id',
        'close_date',
        'fully_invested',
        'invested_amount',
    }
)
async def get_my_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Получает список всех пожертвований для текущего пользователя."""
    user_donations = await donation_crud.get_by_user(
        user, session)
    return user_donations
