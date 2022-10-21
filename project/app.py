from fastapi import FastAPI, Body
from pydantic import BaseModel
from preprocessing.cleaning_data import Cleaning_data
from predict.prediction import Prediction
#import uvicorn

'''
run api locally, from inside directory: $ uvicorn app:app --reload
'''

app = FastAPI()
prediction = Prediction()
cleaning_data = Cleaning_data()

class Data(BaseModel):
  area: int
  property_type: str
  rooms_number: int
  zip_code: int 
  land_area: int | None = 0
  garden: bool | None = False
  garden_area: int | None = 0
  equipped_kitchen: bool | None = None
  full_address: str | None = None
  swimming_pool: bool | None = False
  furnished: bool | None = False
  open_fire: bool | None = False
  terrace: bool | None = False
  terrace_area: int | None = 0
  facades_number: int | None = None
  building_state: str | None = None


@app.get("/")
def root():
    return "alive"

@app.get("/predict")
def predict_info():
  response = {
    "data" : {
      "area": "int",
      "property_type": "APARTMENT | HOUSE | OTHERS",
      "rooms_number": "int",
      "zip_code": "int",
      "land_area": "int | None",
      "garden": "bool | None",
      "garden_area": "int | None",
      "equipped_kitchen": "bool | None",
      "full_address": "str | None",
      "swimming_pool": "bool | None",
      "furnished": "bool | None",
      "open_fire": "bool | None",
      "terrace": "bool | None",
      "terrace_area": "int | None",
      "facades_number": "int | None",
      "building_state": "NEW | GOOD | TO RENOVATE | JUST RENOVATED | TO REBUILD | None"
      }
    }

  return response


@app.post("/predict")
def predict(data : Data = Body(embed=True)):
    # data cleaning and preprocessing
    property_data = data.dict()
    cleaned_property_data = cleaning_data.preprocess(property_data)

    # price prediction
    price_prediction = prediction.predict(cleaned_property_data)

    # create price prediction response
    response = {
      "prediction": price_prediction,
      "status_code": 200 # TODO not hard-coded
    }

    return response


#if __name__ == "__main__":
#  uvicorn.run(app,host="127.0.0.1", port="8000")