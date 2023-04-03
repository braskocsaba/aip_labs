from sqlmodel import Session, select
from models import Coupon
from typing import List, Union
from logger import logger


def get_all_coupons_from_db(session: Session) -> Union[List[Coupon], None]:
    try:
        statement = select(Coupon)
        coupons = session.exec(statement).all()
        logger.info(f"Succeed to retrieve all coupons")
        return coupons
    except Exception as e:
        logger.error(f"Failed to retrieve all coupons, error: {e}")
        return None


def get_coupon_from_db(session: Session, coupon_id: int) -> Union[Coupon, None]:
    try:
        statement = select(Coupon).where(Coupon.id == coupon_id)
        coupon = session.exec(statement).first()
        logger.info(f"Succeed to retrieve the coupon with id: {coupon_id}")
        return coupon
    except Exception as e:
        logger.error(f"Failed to retrieve the coupon with id: {coupon_id}, error: {e}")
        return None


def set_coupon_in_db(session: Session, coupon_id: int, coupon: Coupon) -> Union[Coupon, None]:
    try:
        statement = select(Coupon).where(Coupon.id == coupon_id)
        old_coupon = session.exec(statement).first()
        old_coupon.used = coupon.used
        session.commit()
        statement = select(Coupon).where(Coupon.id == coupon_id)
        new_coupon = session.exec(statement).first()
        logger.info(f"Succeed set the coupon with id id: {coupon_id} to used {coupon.used}")
        return new_coupon
    except Exception as e:
        logger.error(f"Failed to set the coupon with id: {coupon_id} to used {coupon.used}, error: {e}")
        return None
