import json


def preprocess(kwargs) -> json:
    """
    This function will be able to take all the input from the user as Json file and clean it. 
    """
    if kwargs["zip_code"] == 1500:
        kwargs["Bruxelles"] = 1
    else:
        kwargs["Bruxelles"] = 0
    
    if type(kwargs["Livable surface"]) != int:
        return False

    return kwargs