from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.GroupSessionWaitingList])
def read_group_session_waiting_list(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve group session waiting lists.
    """
    if crud.user.is_superuser(current_user):
        group_session_waiting_lists = crud.group_session_waiting_list.get_multi(db, skip=skip, limit=limit)
    else:
        group_session_waiting_lists = crud.group_session_waiting_list.get_multi_by_student(
            db=db, student_id=current_user.id, skip=skip, limit=limit
        )
    return group_session_waiting_lists


@router.post("/", response_model=schemas.GroupSessionWaitingList)
def create_group_session_waiting_list(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_student),
) -> Any:
    """
    Create new group session waiting list.
    """
    if len(crud.group_session_waiting_list.get_multi_by_student(db=db, student_id=current_user.id)) > 0:
        raise HTTPException(status_code=403, detail="Already in a group session waiting list")

    english_level_from_user = models.group_session_waiting_list.ProficiencyLevel.beginner  # dummy level

    group_session_waiting_list_in = schemas.GroupSessionWaitingListInDBCreate(
        student_id=current_user.id, english_proficiency=english_level_from_user
    )
    group_session_waiting_list = crud.group_session_waiting_list.create(db=db, obj_in=group_session_waiting_list_in)
    return group_session_waiting_list


@router.get("/{id}", response_model=schemas.GroupSessionWaitingList)
def read_group_session_waiting_list(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get group session waiting list by ID.
    """
    group_session_waiting_list = crud.group_session_waiting_list.get(db=db, id=id)
    if not group_session_waiting_list:
        raise HTTPException(status_code=404, detail="group_session_waiting_list not found")
    if not crud.user.is_superuser(current_user) and (group_session_waiting_list.student_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return group_session_waiting_list


@router.delete("/{id}", response_model=schemas.GroupSessionWaitingList)
def delete_group_session_waiting_list(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a group session waiting list.
    """
    group_session_waiting_list = crud.group_session_waiting_list.get(db=db, id=id)
    if not group_session_waiting_list:
        raise HTTPException(status_code=404, detail="group_session_waiting_list not found")
    if not crud.user.is_superuser(current_user) and (group_session_waiting_list.student_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    group_session_waiting_list = crud.group_session_waiting_list.remove(db=db, id=id)
    return group_session_waiting_list
