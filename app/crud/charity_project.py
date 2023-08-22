from typing import Optional, List

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> List[CharityProject]:
        closed_projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == True, # noqa
            ).order_by(
                func.strftime('%s', CharityProject.close_date)
                - func.strftime('%s', CharityProject.create_date))
        )
        # не сортирует по timedelta никак не срабатывает, strftime должен помочь, но все равно сортировка не происходит
        closed_projects = closed_projects.scalars().all()
        return closed_projects


charity_project_crud = CRUDCharityProject(CharityProject)
