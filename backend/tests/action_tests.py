import pytest
from datetime import timezone
import datetime
from models import Action


@pytest.fixture()
def create_percent_discount_action(db_session_test):
    action_1 = Action(type="percent discount action",
                      name="summer action 2023 Hungary",
                      description="summer action 2023 Hungary",
                      valid_until=datetime.datetime.now(timezone.utc) + datetime.timedelta(days=21),
                      discount_percent=10,
                      discount_value_currency="HUF",
                      discount_value=0
                      )

    db_session_test.add(action_1)
    db_session_test.commit()
    yield action_1

    db_session_test.delete(action_1)
    db_session_test.commit()


@pytest.fixture()
def create_value_discount_action(db_session_test):
    action_1 = Action(type="value discount action",
                      name="summer action 2023 Hungary",
                      description="summer action 2023 Hungary",
                      valid_until=datetime.datetime.now(timezone.utc) + datetime.timedelta(days=21),
                      discount_percent=0,
                      discount_value_currency="HUF",
                      discount_value=1000
                      )

    db_session_test.add(action_1)
    db_session_test.commit()
    yield action_1

    db_session_test.delete(action_1)
    db_session_test.commit()
