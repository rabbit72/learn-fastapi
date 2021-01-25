from .crud_item import item
from .crud_user import user
from .crud_group_session_waiting_list import group_session_waiting_list
from .crud_individual_lesson_plan import individual_lesson_plan

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
