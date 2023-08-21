from sqlalchemy import Column, String, Text

from app.core.constants import STR_FIELD_MAX_LENGTH

from .base import ProjectDonation


class CharityProject(ProjectDonation):
    name = Column(String(STR_FIELD_MAX_LENGTH), unique=True, nullable=False)
    description = Column(Text, nullable=False)
