from typing import TYPE_CHECKING
from enum import Enum
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime, Enum as EnumType
from sqlalchemy.sql import func

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class ProficiencyLevel(Enum):
    beginner = 1
    elemenary = 2


class GroupSessionWaitingList(Base):
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(ForeignKey("user.id"), unique=True)
    english_proficiency = Column(EnumType(ProficiencyLevel), nullable=False)

    updated = Column(DateTime, onupdate=func.now())
    created = Column(DateTime, server_default=func.now())
