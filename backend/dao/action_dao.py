from sqlmodel import Session, select
from models import Action
from typing import List, Union
from logger import logger


def get_all_actions_from_db(session: Session) -> Union[List[Action], None]:
    try:
        statement = select(Action)
        actions = session.exec(statement).all()
        logger.info(f"Succeed to retrieve all actions")
        return actions
    except Exception as e:
        logger.error(f"Failed to retrieve all actions, error: {e}")
        return None


def get_action_from_db(session: Session, action_id: int) -> Union[Action, None]:
    try:
        statement = select(Action).where(Action.id == action_id)
        action = session.exec(statement).first()
        logger.info(f"Succeed to retrieve the action with id: {action_id}")
        return action
    except Exception as e:
        logger.error(f"Failed to retrieve the action with id: {action_id}, error: {e}")
        return None

