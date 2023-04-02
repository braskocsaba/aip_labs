from db import session_manager
from models import Coupon
from sqlmodel import select
from typing import List, Union
from dao.coupon_dao import get_all_coupons_from_db

def get_all_coupons() -> Union[List[Coupon], None]:
    """
    Get all coupons stored in database
    """
    with session_manager() as session:
        return get_all_coupons_from_db(session)


def get_coupon(coupon_id: int) -> dict:
    """
    Get specific coupon stored in the database
    """
    pass


def create_coupon() -> dict:
    """
    create coupon from data in the parameter and store in the database
    """
    pass

