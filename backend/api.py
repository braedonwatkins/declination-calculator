from fastapi import FastAPI
from pydantic import BaseModel

import numpy as np
import math

from .calc.core import field_vector

latMin, latMax = -90, 90
lonMin, lonMax = -180, 180

app = FastAPI()


@app.get("/")
async def default():
    return "Ready 3 Biznes"


class Test(BaseModel):
    lat: float
    lon: float
    h: float
    year: float


@app.post("/point-calc")
async def point_calc(req: Test):
    vector = field_vector(req.lat, req.lon, req.h, req.year)
    vector.I = math.degrees(vector.I)
    vector.D = math.degrees(vector.D)

    return {"message": "success", "vector": vector}


class Test2(BaseModel):
    lat_lon_list: list[float]
    h: float
    year: float


@app.post("/vector-field")
async def vector_field(req: Test2):
    lat_lon_list = req.lat_lon_list

    vectors = []

    for i in range(0, len(lat_lon_list), 2):
        lat, lon = lat_lon_list[i], lat_lon_list[i + 1]
        vec = field_vector(lat, lon, req.h, req.year)
        vec.I = math.degrees(vec.I)
        vec.D = math.degrees(vec.D)

        vectors.append(vec)

    return {"message": "success", "vectors": vectors}
