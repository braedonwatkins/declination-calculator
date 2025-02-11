from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from .calc.core import field_vector

app = FastAPI()


class Test(BaseModel):
    lat: float
    lon: float
    h: float
    year: float


@app.get("/")
async def default():
    return "Ready 3 Biznes"


@app.post("/point-calc")
async def point_calc(req: Test):
    test = field_vector(req.lat, req.lon, req.h, req.year)
    return {"RESULT": test}
