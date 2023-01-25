import urllib.request

import cloudpickle
import pandas as pd
from sklearn.pipeline import Pipeline


def load_model(url: str) -> Pipeline:
    #file = urllib.request.urlopen(url)
    file=open(url, "rb")
    model = cloudpickle.load(file)

    # if not model_loaded_correctly(model):
    # raise Exception("Missmatch in predictions detected!")

    return model



