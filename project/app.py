from fastapi import FastAPI
from pydantic import BaseModel
from preprocessing.cleaning_data import Cleaning_data

'''
run api locally, from inside directory: $ uvicorn app:app --reload
'''

app = FastAPI()

class Property(BaseModel):
  area: int
  property_type: str
  rooms_number: int
  zip_code: int 
  land_area: int | None = None
  garden: bool | None = None
  garden_area: int | None = None
  equipped_kitchen: bool | None = None
  full_address: str | None = None
  swimming_pool: bool | None = None
  furnished: bool | None = None
  open_fire: bool | None = None
  terrace: bool | None = None
  terrace_area: int | None = None
  facades_number: int | None = None
  building_state: str | None = None


@app.get("/")
def root():
    return {"message":"alive"}


@app.post("/predict")
def predict(property : Property):
    property_data = property.dict()
    cleaning_data = Cleaning_data()
    cleaning_data.preprocess(property_data)
    return {"message" : property}

'''
INPUT JSON
{
  "data": {
    "area": int,
    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
    "rooms-number": int,
    "zip-code": int,
    "land-area": Optional[int],
    "garden": Optional[bool],
    "garden-area": Optional[int],
    "equipped-kitchen": Optional[bool],
    "full-address": Optional[str],
    "swimming-pool": Optional[bool],
    "furnished": Optional[bool],
    "open-fire": Optional[bool],
    "terrace": Optional[bool],
    "terrace-area": Optional[int],
    "facades-number": Optional[int],
    "building-state": Optional[
      "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
    ]
  }
}

OUTPUT JSON
{
  "prediction": Optional[float],
  "status_code": Optional[int]
}

'''