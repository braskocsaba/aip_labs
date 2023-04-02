from sqlmodel import Session, select
from models import Coupon
from typing import List, Union
from logger import logger


def get_all_coupons_from_db(db: Session) -> Union[List[Coupon], None]:
    try:
        statement = select(Coupon)
        result = db.exec(statement).all()
        logger.info(f"Succeed to retrieve all coupons")
        return result
    except Exception as e:
        logger.error(f"Failed to retrieve all coupons, error: {e}")
        return None


def get_coupons_from_db(db: Session, id:int) -> Union[List[Coupon], None]:
    try:
        statement = select(Coupon).where(Coupon.id == id)
        result = db.exec(statement).one_or_none()
        logger.info(f"Succeed to retrieve the coupon with id")
        return result
    except Exception as e:
        logger.error(f"Failed to retrieve all coupons, error: {e}")
        return None
