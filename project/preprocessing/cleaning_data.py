import typing
from typing import Any

property_types: list[str]
building_states: list[str]

class Cleaning_data:

    def __init__(self):
        self.property_types = ['HOUSE', 'APARTMENT']
        self.building_states = ["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"]


    def preprocess(self, property_data: Any):   
        # check mandatory data, return error if not valid
        
        error_message = self.validate_property_data(property_data)
        
        if len(error_message) > 0:
            raise RuntimeError(error_message)

        #preprocess property data


        #return a np.array with features X to the model  


    def validate_property_data(self, property_data: Any):

        message = ''

        if property_data['area'] < 1:
            message = "Property area must be bigger than 0"

        elif property_data['property_type'] not in self.property_types:
            message = "Property type must be specified"
        
        elif property_data["building_state"] not in self.building_states:
            message = "Building state must be specified"

        elif property_data['zip_code'] < 1000 or property_data['zip_code'] > 9999:
            message = "Zip code must have 4 digits"

        return message