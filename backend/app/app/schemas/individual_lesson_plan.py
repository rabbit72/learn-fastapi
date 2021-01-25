from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel


# Shared properties
class IndividualLessonPlanBase(BaseModel):
    start_day: Optional[date] = None


# Properties to receive via API on creation
class IndividualLessonPlanCreate(IndividualLessonPlanBase):
    start_day: date


# Properties to receive via API on update
class IndividualLessonPlanUpdate(IndividualLessonPlanBase):
    teacher_id: Optional[int] = None


class IndividualLessonPlanInDBBase(IndividualLessonPlanBase):
    id: int
    student_id: int
    teacher_id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class IndividualLessonPlan(IndividualLessonPlanInDBBase):
    pass


# Additional properties stored in DB
class IndividualLessonPlanInDB(IndividualLessonPlanInDBBase):
    created: datetime
    updated: datetime
