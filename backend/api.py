from dataclasses import dataclass
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

import math

from .my_types import FieldVector


from .calc.core import field_vector
from fastapi.middleware.cors import CORSMiddleware

latMin, latMax = -90, 90
lonMin, lonMax = -180, 180

app = FastAPI()

origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)


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


@dataclass
class RetVec(FieldVector):
    lat: Optional[float] = None
    lon: Optional[float] = None


@app.post("/vector-field")
async def vector_field(req: Test2):
    lat_lon_list = req.lat_lon_list

    vectors = []

    for i in range(0, len(lat_lon_list), 2):
        lat, lon = lat_lon_list[i], lat_lon_list[i + 1]
        vec = field_vector(lat, lon, req.h, req.year)
        vec.I = math.degrees(vec.I)
        vec.D = math.degrees(vec.D)

        # NOTE: this seems like a silly way to extend a class but i'll let it go for now
        ret: RetVec = RetVec(**vec.__dict__, lat=lat, lon=lon)

        vectors.append(ret)

    return {"message": "success", "vectors": vectors}
