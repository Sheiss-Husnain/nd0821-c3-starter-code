import json

import requests
data = {
  "age": 25,
  "workclass": "Self-emp-not-inc",
  "fnlgt": 176756,
  "education": "HS-grad",
  "education-num": 9,
  "marital-status": "Never-married",
  "occupation": "Farming-fishing",
  "relationship": "Own-child",
  "race": "White",
  "sex": "Male",
  "capital-gain": 0,
  "capital-loss": 0,
  "hours-per-week": 40,
  "native-country": "United-States"
}

#<=50k
response = requests.post('https://sheiss-census.herokuapp.com/predict/', json=data)
#response = client.post("/predict", json=data)
print(response.status_code)
print(response.json())
