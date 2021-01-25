from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from app.models.group_session_waiting_list import ProficiencyLevel


# Properties to receive via API on creation
class GroupSessionWaitingListCreate(BaseModel):
    pass


# Properties to receive via API on update
class GroupSessionWaitingListUpdate(BaseModel):
    pass


class GroupSessionWaitingListInDBCreate(BaseModel):
    student_id: int
    english_proficiency: ProficiencyLevel


class GroupSessionWaitingListInDBBase(BaseModel):
    id: int
    student_id: int
    english_proficiency: ProficiencyLevel

    class Config:
        orm_mode = True


# Additional properties to return via API
class GroupSessionWaitingList(GroupSessionWaitingListInDBBase):
    pass


# Additional properties stored in DB
class GroupSessionWaitingListInDB(GroupSessionWaitingListInDBBase):
    created: datetime
    updated: datetime
