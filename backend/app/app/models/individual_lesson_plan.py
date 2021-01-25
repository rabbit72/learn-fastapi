from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.sql import func

from app.db.base_class import Base
from .user import User



class IndividualLessonPlan(Base):
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(ForeignKey(User.id))
    teacher_id = Column(ForeignKey(User.id))

    updated = Column(DateTime, onupdate=func.now())
    created = Column(DateTime, server_default=func.now())

    __table_args__ = (UniqueConstraint(student_id, teacher_id, name="student_teacher_duplicate"),)