from fastapi import FastAPI
from .src.os_info import get_os_info
from .src.models import DoubleProductRequest
from .src.algorithms import calculate_rpp

app = FastAPI()

@app.get("/management/get-os-info")
async def get_info_route():
    return get_os_info()

@app.post("/processing/calculate-rpp")
async def calculate_rpp_route(request: DoubleProductRequest):
    return calculate_rpp(request.hr, request.sbp)