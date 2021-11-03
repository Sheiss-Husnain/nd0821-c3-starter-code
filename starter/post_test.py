import json

import requests
data = {
  "age": 39,
  "workclass": "State-gov",
  "fnlgt": 77516,
  "education": "Bachelors",
  "education-num": 13,
  "marital-status": "Never-married",
  "occupation": "Adm-clerical",
  "relationship": "Not-in-family",
  "race": "White",
  "sex": "Male",
  "capital-gain": 2174,
  "capital-loss": 0,
  "hours-per-week": 40,
  "native-country": "United-States"
}
# data= {
        # "age": 25,
        # "workclass": "Self-emp-not-inc",
        # "fnlgt": 176756,
        # "education": "HS-grad",
        # "education_num": 9,
        # "marital_status": "Never-married",
        # "occupation": "Farming-fishing",
        # "relationship": "Own-child",
        # "race": "White",
        # "sex": "Male",
        # "capital_gain": 0,
        # "capital_loss": 0,
        # "hours_per_week": 35,
        # "native_country": "United-States"
#       }
#<=50k
response = requests.post('https://sheiss-census.herokuapp.com/predict/', json=data)
#response = client.post("/predict", json=data)
print(response)