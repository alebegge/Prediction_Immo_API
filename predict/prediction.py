import json
import pandas as pd
import numpy as np
import sys
# from model.price_pred_model import features

features = [
    "Livable surface",
    "Type property",
    "Brussels",
    "Walloon Brabant",
    "Flemish Brabant",
    "Antwerp",
    "Limburg",
    "Liege",
    "Namur",
    "Luxembourg",
    "Hainaut",
    "West Flanders",
    "East Flanders",
    "Kitchen equipment",
    "State of the property",
    "Furnished",
    "Number of facades",
    "Surface terrace",
    "Surface garden"
]
json_out =  {
        "East Flanders": 1,
        "Furnished": 0,
        "Kitchen equipment": 2,
        "Livable surface": 150,
        "Number of facades": 2,
        "State of the property": 1,
        "Surface garden": 0,
        "Surface terrace": 0,
        "Type property": 1
    }

df_test = pd.DataFrame(columns=features)
df_test = df_test.append(json_out,ignore_index=True)
df_test = df_test.fillna(0)

def predict(json_input) -> json:
    """
    Return a predict price based on json input by the user.
    """
    # json_output = {}
    # json_output["data"] = json_input
    # return json_output
    df_test = pd.DataFrame(columns=features)
    df_test = df_test.append(json_out,ignore_index=True)
    df_test = df_test.fillna(0)
    return df_test.to_dict('split')