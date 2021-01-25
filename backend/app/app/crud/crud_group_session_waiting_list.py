from sqlalchemy.orm import Session
from typing import List
from app.crud.base import CRUDBase
from app.models import GroupSessionWaitingList
from app.schemas import GroupSessionWaitingListInDBCreate, GroupSessionWaitingListUpdate


class CRUDGroupSessionWaitingList(
    CRUDBase[GroupSessionWaitingList, GroupSessionWaitingListInDBCreate, GroupSessionWaitingListUpdate]
):
    def create_with_student(
        self, db: Session, *, obj_in: GroupSessionWaitingListInDBCreate, student_id: int
    ) -> GroupSessionWaitingList:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, student_id=student_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_student(
        self, db: Session, *, student_id: int, skip: int = 0, limit: int = 100
    ) -> List[GroupSessionWaitingList]:
        return (
            db.query(self.model)
            .filter(GroupSessionWaitingList.student_id == student_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


group_session_waiting_list = CRUDGroupSessionWaitingList(GroupSessionWaitingList)