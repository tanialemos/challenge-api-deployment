import pickle
from typing import Dict
import pandas as pd

class Prediction:

    def __init__(self) -> None:
        with open("model/saved_model.pkl", 'rb') as file:
            data = pickle.load(file)
            self.model = data['model']
    
    def predict(self, cleaned_property_data: Dict):

        ready_property_data = {}
        for key, value in cleaned_property_data.items():
            ready_property_data[key] = [value]
        
        print(ready_property_data)
        X = pd.DataFrame.from_dict(ready_property_data)

        prediction = self.model.predict(X)
        if prediction.size != 1:
            raise RuntimeError("Some error with prediction")

        return prediction[0]