import json


def predict(json_input) -> json:
    """
    Return a predict price based on json input by the user.
    """
    json_output = {}
    json_output["data"] = json_input
    return json_output

