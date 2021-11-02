import json

import requests
data = {
                "age": 22,
                "workclass": "Private",
                "fnlgt": 201490,
                "education": "HS-grad",
                "education_num": 9,
                "marital_status": "Never-married",
                "occupation": "Adm-clerical",
                "relationship": "Own-child",
                "race": "White",
                "sex": "Male",
                "capital_gain": 0,
                "capital_loss": 0,
                "hours_per_week": 20,
                "native_country": "United-States"
                }
# data= {
#         "age": 25,
#         "workclass": "Self-emp-not-inc",
#         "fnlgt": 176756,
#         "education": "HS-grad",
#         "education_num": 9,
#         "marital_status": "Never-married",
#         "occupation": "Farming-fishing",
#         "relationship": "Own-child",
#         "race": "White",
#         "sex": "Male",
#         "capital_gain": 0,
#         "capital_loss": 0,
#         "hours_per_week": 35,
#         "native_country": "United-States"
#       }
#<=50k
response = requests.post('https://sheiss-census.herokuapp.com/predict/', data=json)

print(response.status_code)
print(response.json())