from typing import Dict, List

import numpy as np
import pandas as pd
from fastapi import FastAPI
from numpy.typing import NDArray

from src.models import car, recipe, tweet
from src.utilsx.model_utils import load_model

import cloudpickle
import urllib.request
# loading model


direktorija="C:\\Users\\stabu\\My Drive\\05. Dirbtinis intelektas\\ML\\ML-tveets-about-Ukrain-analysis\\src\\models\\tweet_model.pkl"

tweet_model = load_model(direktorija)

    








tweet_model = cloudpickle.load(file)



app = FastAPI()



@app.get("/health")
def health() -> Dict[str, str]:
    return {"health": "alive"}

@app.post("/predict_tweets")
def predict_tweets(inputs: List[tweet.Input]) -> Dict[str, List[Dict[str, float]]]:
    parsed_input = pd.DataFrame([i.dict() for i in inputs])
    outputs: NDArray[np.float32] = tweet_model.predict(parsed_input["text"].values)

    return {"outputs": [{"class": i} for i in outputs.tolist()]}
