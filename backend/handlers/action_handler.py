from db import session_manager
from models import Coupon, Action
from sqlmodel import select
from typing import List, Union
from dao.action_dao import get_all_actions_from_db, get_action_from_db


def get_all_actions() -> Union[List[Action], None]:
    """
    Get all actions stored in database
    """
    with session_manager() as session:
        return get_all_actions_from_db(session)


def get_action(action_id: int) -> Union[Action, None]:
    """
    Get specific action stored in the database
    """
    with session_manager() as session:
        return get_action_from_db(session, action_id)

