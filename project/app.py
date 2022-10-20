from fastapi import FastAPI
from pydantic import BaseModel
from preprocessing.cleaning_data import Cleaning_data
from predict.prediction import Prediction
import uvicorn

'''
run api locally, from inside directory: $ uvicorn app:app --reload
'''

app = FastAPI()

class Property(BaseModel):
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
    return {"message":"alive"}


@app.post("/predict")
def predict(property : Property):
    # data cleaning and preprocessing
    property_data = property.dict()
    cleaning_data = Cleaning_data()
    cleaned_property_data = cleaning_data.preprocess(property_data)

    # price prediction
    prediction = Prediction()
    price_prediction = prediction.predict(cleaned_property_data)

    # create price prediction response
    response = {
      "prediction": price_prediction,
      "status_code": 200 # TODO not hard-coded
    }

    return {"message" : response}


#if __name__ == "__main__":
#  uvicorn.run(app,host="127.0.0.1", port="8000")