from starter.ml.data import process_data
from starter.ml.model import inference

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel, Field

import pandas as pd
import numpy as np
import os

model_dir = "starter/model/"
model_file = model_dir+"model.pkl"
encoding_file = model_dir+"encoder.pkl"
lb_file = model_dir+'lb.pkl'



app = FastAPI()
model = pd.read_pickle(model_file)
Encoder = pd.read_pickle(encoding_file)
lb_ = pd.read_pickle(lb_file)

if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")

class Input(BaseModel):
    age: int = Field(..., example=39)
    workclass: str = Field(..., example="State-gov")
    fnlgt: int = Field(..., example=77516)
    education: str = Field(..., example="Bachelors")
    education_num: int = Field(..., example=13, alias="education-num")
    marital_status: str = Field(..., example="Never-married", alias="marital-status")
    occupation: str = Field(..., example="Adm-clerical")
    relationship: str = Field(..., example="Not-in-family")
    race: str = Field(..., example="White")
    sex: str = Field(..., example="Male")
    capital_gain: int = Field(..., example=2174, alias="capital-gain")
    capital_loss: int = Field(..., example=0, alias="capital-loss")
    hours_per_week: int = Field(..., example=40, alias="hours-per-week")
    native_country: str = Field(..., example="United-States", alias="native-country")

class Output(BaseModel):
    predict: str = "Income > 50k"

@app.get("/")
async def root():
    return {"Welcome to Census Model"}

@app.post("/predict", response_model=Output, status_code=200)
def get_predicition(payload: Input):
    df = pd.DataFrame.from_dict([payload.dict(by_alias=True)])

    # age = payload.age
    # workclass = payload.workclass
    # fnlgt = payload.fnlgt
    # education = payload.education
    # education_num = payload.education_num
    # marital_status = payload.marital_status
    # occupation = payload.occupation
    # relationship = payload.relationship
    # race = payload.race
    # sex = payload.sex
    # capital_gain = payload.capital_gain
    # capital_loss = payload.capital_loss
    # hours_per_week = payload.hours_per_week
    # native_country = payload.native_country

    # df = pd.DataFrame({"age" : age,
    #                     "workclass" : workclass,
    #                     "fnlgt" : fnlgt,
    #                     "education" : education,
    #                     "education-num" : education_num,
    #                     "marital-status" : marital_status,
    #                     "occupation" : occupation,
    #                     "relationship" : relationship,
    #                     "race" : race,
    #                     "sex" : sex,
    #                     "capital-gain" : capital_gain,
    #                     "capital-loss" : capital_loss,
    #                     "hours-per-week" : hours_per_week,
    #                     "native-country" : native_country})

    cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country"]

    X, y, encoder, lb = process_data(df, categorical_features=cat_features, training=False,encoder=Encoder,lb=lb_)

    prediction = inference(model, X)

    if prediction==1: prediction = "Income > 50k"
    elif prediction==0: prediction = "Income <= 50k"

    r = {"predict": prediction}

    return r