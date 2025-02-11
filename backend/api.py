from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from .calc.core import field_vector

app = FastAPI()


class Location(BaseModel):
    lat: float
    lon: float
    h: float


@app.get("/")
async def default():
    return "Ready 3 Biznes"


@app.get("/point-calc")
async def point_calc(location: Location):
    return "TODO: finish!"
