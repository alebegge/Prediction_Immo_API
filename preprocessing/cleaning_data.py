import json


def preprocess(input_json) -> json:
    """
    This function will be able to take all the input from the user as Json file and clean it. 
    erreur custom -> class from inerhit (flask ?)
    """

    # df = df.drop(df[df['Livable surface'].isna()].index)
    # df = df.drop(df[df['Livable surface'] > 2000].index)
    predict_dict = {}

    if 0 < input_json["area"] < 2000:
        predict_dict["Livable surface"] = input_json["area"]

    # if kwargs["zip_code"] == 1500:
    #     kwargs["Bruxelles"] = 1
    # else:
    #     kwargs["Bruxelles"] = 0
    
    # if type(kwargs["Livable surface"]) != int:
    #     return False
    # if kwargs["toilets"] > 6:
    #     return False

    return input_json