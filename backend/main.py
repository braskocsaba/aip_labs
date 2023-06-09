#third party imports
from fastapi import FastAPI, status
import uvicorn

from handlers.coupon_handler import get_all_coupons, get_coupon, set_coupon
from handlers.action_handler import get_all_actions, get_action
from typing import List
from models import Coupon, Action


app = FastAPI()

# R O U T E - H A N D L E R   P A I R S
app.get("/api/v1/coupons/", tags=["Coupon"], response_model=List[Coupon], status_code=status.HTTP_200_OK)(get_all_coupons)
app.get("/api/v1/coupon/{coupon_id}", tags=["Coupon"], response_model=Coupon, status_code=status.HTTP_200_OK)(get_coupon)
app.put("/api/v1/coupon/{coupon_id}", tags=["Coupon"], response_model=Coupon, status_code=status.HTTP_200_OK)(set_coupon)

app.get("/api/v1/actions/", tags=["Action"], response_model=List[Action], status_code=status.HTTP_200_OK)(get_all_actions)
app.get("/api/v1/actions/{actions_id}", tags=["Action"], response_model=Action, status_code=status.HTTP_200_OK)(get_action)


def main():
    uvicorn.run('main:app', host="0.0.0.0", port=3333, reload=True, reload_dirs=['/backend'])


if __name__ == "__main__":
    main()
