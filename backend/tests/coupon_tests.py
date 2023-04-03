import pytest
from models import Coupon
from dao.coupon_dao import get_all_coupons_from_db, get_coupon_from_db, set_coupon_in_db


@pytest.fixture()
def create_coupons(db_session_test):
    coupon_1 = Coupon(used=False)
    coupon_2 = Coupon(used=True)
    db_session_test.add(coupon_1)
    db_session_test.add(coupon_2)
    db_session_test.commit()

    yield coupon_1, coupon_2

    db_session_test.delete(coupon_1)
    db_session_test.delete(coupon_2)
    db_session_test.commit()


def test_get_all_coupon_from_db(db_session_test, create_coupons):
    coupon_1, coupon_2 = create_coupons
    coupons = get_all_coupons_from_db(db_session_test)
    assert len(coupons) > 1


def test_get_coupon_from_db(db_session_test, create_coupons):
    coupon_1, coupon_2 = create_coupons

    assert coupon_1.id == get_coupon_from_db(db_session_test, coupon_1.id).id
    assert coupon_1.used == get_coupon_from_db(db_session_test, coupon_1.id).used

    assert coupon_2.id == get_coupon_from_db(db_session_test, coupon_2.id).id
    assert coupon_2.used == get_coupon_from_db(db_session_test, coupon_2.id).used


def test_set_coupon_to_used(db_session_test, create_coupons):
    coupon_1, coupon_2 = create_coupons
    assert set_coupon_in_db(db_session_test, coupon_1.id, coupon_2).used
    assert set_coupon_in_db(db_session_test, coupon_2.id, coupon_2).used

    coupon_3, coupon_4 = create_coupons
    assert set_coupon_in_db(db_session_test, coupon_4.id, coupon_3).used
    assert set_coupon_in_db(db_session_test, coupon_3.id, coupon_4).used
