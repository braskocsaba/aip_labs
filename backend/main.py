from fastapi import FastAPI
import uvicorn

from handlers.coupon_handler import get_all_coupons, get_coupon, create_coupon

app = FastAPI()

# R O U T E - H A N D L E R   P A I R S
app.get("/api/v1/coupons/", tags=["Coupon"])(get_all_coupons)
app.get("/api/v1/coupon/{coupon_id}", tags=["Coupon"])(get_coupon)
app.post("/api/v1/coupon/{coupon_id}", tags=["Coupon"])(create_coupon)

def main():
    uvicorn.run('main:app', host="0.0.0.0", port=3333, reload=True, reload_dirs=['/backend'])


if __name__ == "__main__":
    main()
