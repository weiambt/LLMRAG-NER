import json

def exratct(input):
    dict = json.loads(input)
    return dict["text"],dict["label"]