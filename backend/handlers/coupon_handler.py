from db import session_manager
from models import Coupon
from sqlmodel import select
from typing import List, Union
from dao.coupon_dao import get_all_coupons_from_db, get_coupon_from_db, set_coupon_used_in_db


def get_all_coupons() -> Union[List[Coupon], None]:
    """
    Get all coupons stored in database
    """
    with session_manager() as session:
        return get_all_coupons_from_db(session)


def get_coupon(coupon_id: int) -> Union[Coupon, None]:
    """
    Get specific coupon stored in the database
    """
    with session_manager() as session:
        return get_coupon_from_db(session, coupon_id)


def set_coupon(coupon_id: int) -> Union[Coupon, None]:
    """
    Set specific coupon to used and store it in the database
    """
    with session_manager() as session:
        return set_coupon_used_in_db(session, coupon_id)

