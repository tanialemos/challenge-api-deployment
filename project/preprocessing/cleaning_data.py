import typing
from typing import Any

property_types: list[str]
building_states: list[str]

class Cleaning_data:

    def __init__(self):
        self.property_types = ['HOUSE', 'APARTMENT']
        self.building_states = ["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"]


    def preprocess(self, property_data: Any) -> Any:   
        # check mandatory data, return error if not valid
        
        error_message = self.validate_property_data(property_data)
        
        if len(error_message) > 0:
            raise RuntimeError(error_message)
    # expected X:
    #['type_of_property', 'number_of_bedrooms', 'surface', 'terrace',
    #       'garden', 'swimming_pool', 'state_of_the_building',
    #       'postal_code_score']
        # drop unnecessary features
        property_data.pop('land_area')
        property_data.pop('garden_area')
        property_data.pop('equipped_kitchen')
        property_data.pop('full_address')
        property_data.pop('furnished')
        property_data.pop('open_fire')
        property_data.pop('terrace_area')
        property_data.pop('facades_number')
        property_data.pop('zip_code') # TODO

        # rename and reorder dictionnary keys to match model features
        property_data['type_of_property'] = property_data.pop('property_type')
        property_data['number_of_bedrooms'] = property_data.pop('rooms_number')
        property_data['surface'] = property_data.pop('area')
        property_data['terrace'] = property_data.pop('terrace')
        property_data['garden'] = property_data.pop('garden')
        property_data['swimming_pool'] = property_data.pop('swimming_pool')
        property_data['state_of_the_building'] = property_data.pop('building_state')
        #property_data['postal_code_score'] = property_data.pop('zip_code')

        # translate categories into numeric values
        property_data["type_of_property"] = 1 if property_data["type_of_property"] == "HOUSE" else 0
        property_data["state_of_the_building"] = 0 if property_data["state_of_the_building"] == "TO RENOVATE" or property_data["state_of_the_building"] == "TO RESTORE" else 1


        return property_data  


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