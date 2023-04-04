from datetime import timezone
import datetime
from models import Coupon, Action
from sqlmodel import Session


def create_percent_discount_action(session: Session):
    action_1 = Action(type="percent discount action",
                      name="summer action 2023 Hungary",
                      description="summer action 2023 Hungary",
                      valid_until=datetime.datetime.now(timezone.utc) + datetime.timedelta(days=21),
                      discount_percent=10,
                      discount_value_currency="HUF",
                      discount_value=0
                      )

    session.add(action_1)
    session.commit()
    return action_1


def create_value_discount_action(session: Session):
    action_1 = Action(type="value discount action",
                      name="summer action 2023 Hungary",
                      description="summer action 2023 Hungary",
                      valid_until=datetime.datetime.now(timezone.utc) + datetime.timedelta(days=21),
                      discount_percent=0,
                      discount_value_currency="HUF",
                      discount_value=1000
                      )

    session.add(action_1)
    session.commit()
    return action_1


def create_coupons_to_value_discount_action(session: Session):
    action = create_value_discount_action(session)
    id_t = action.id
    coupon_list = []
    for i in range(0,10):
        coupon_list.append(Coupon(used=False, action_id=action.id))
        session.add(coupon_list[i])
    session.commit()


def create_coupons_to_percent_discount_action(session: Session):
    action = create_percent_discount_action(session)
    id_t = action.id
    coupon_list = []
    for i in range(0, 10):
        coupon_list.append(Coupon(used=False, action_id=action.id))
        session.add(coupon_list[i])
    session.commit()

