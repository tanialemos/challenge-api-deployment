from fastapi import FastAPI
from pydantic import BaseModel

'''
run api locally, from inside directory: $ uvicorn app:app --reload
'''

app = FastAPI()


class Data(BaseModel):
  area: int
  property-type: str
  rooms-number: int
  zip-code: int
  land-area: int
  #"garden": bool
  #"garden-area": int
  #"equipped-kitchen": bool
  #"full-address": str


class Property(BaseModel):
  data: Data


@app.get("/")
def root():
    return {"message":"alive"}


@app.post("/predict")
def predict(property : Property):
    return {"message" : property}


"""
# deserialising json
    property = json.loads(api_input)
"""

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