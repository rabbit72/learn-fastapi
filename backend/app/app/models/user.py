from typing import TYPE_CHECKING
from enum import Enum
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Enum as EnumType
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class UserRole(Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True, nullable=False)
    is_superuser = Column(Boolean(), default=False, nullable=False)

    type_ = Column(EnumType(UserRole), nullable=False)
    updated = Column(DateTime, onupdate=func.now())
    created = Column(DateTime, server_default=func.now())
    items = relationship("Item", back_populates="owner")
