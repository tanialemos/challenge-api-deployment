import json
import typing
from typing import Any

def preprocess(property: Any):   
    # check mandatory data, returns error if missing
    property_data = property["property_data"]
    check_mandatory_data(property_data)

    #preprocess property data

    

    #return a np.array with features X to the model  

    pass

def check_mandatory_data(property_data):

    if type(property_data["area"]) != int or property_data["area"] is None:
        raise RuntimeError("Area must be specified")
    
    elif type(property_data["property-type"]) != str or property_data["property-type"] is None:
        raise RuntimeError("Property type must be specified")
    
    elif type(property_data["building-state"]) != str or property_data["building-state"] is None:
        raise RuntimeError("Building state must be specified")

    elif type(property_data["zip-code"]) != int or property_data["zip-code"] is None:
        raise RuntimeError("Zip-code must be specified")