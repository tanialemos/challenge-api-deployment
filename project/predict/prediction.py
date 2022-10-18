import pickle
from typing import Dict
import pandas as pd

class Prediction:

    def __init__(self) -> None:
        pass

    def load_model(self):
        with open("../project/model/saved_model.pkl", 'rb') as file:
            data = pickle.load(file)
        return data


    # expected X:
    #['type_of_property', 'number_of_bedrooms', 'surface', 'terrace',
    #       'garden', 'swimming_pool', 'state_of_the_building',
    #       'postal_code_score']

    def predict(self, cleaned_property_data: Dict):

        ready_property_data = {}
        for key, value in cleaned_property_data.items():
            ready_property_data[key] = [value]
        
        print(ready_property_data)
        X = pd.DataFrame.from_dict(ready_property_data)
        print(X.shape)
        print(X)

        data = self.load_model()

        regressor = data['model']
        #property_type_encoder = data['property_type_encoder']
        #building_state_encoder = data['building_state_encoder']

        prediction = regressor.predict(X)
        print(f'Price prediction is:  {prediction}')


        pass