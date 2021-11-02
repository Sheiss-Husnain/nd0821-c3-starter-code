from main import app

from fastapi.testclient import TestClient
import json
client = TestClient(app)

def test_get():
    response = client.get("/")
    assert response.status_code == 200

def test_post():
    data = {
        "age": 28,
        "workclass": "Private",
        "fnlgt": 338409,
        "education": "Bachelors",
        "education-num": 13,
        "marital-status": "Married-civ-spouse",
        "occupation": "Prof-specialty",
        "relationship": "Wife",
        "race": "Black",
        "sex": "Female",
        "capital-gain": 0,
        "capital-loss": 0,
        "hours-per-week": 40,
        "native-country": "Cuba",
    }
  #  list = [(k, v) for k, v in data.items()]
        #28,Private,338409,Bachelors,13,Married-civ-spouse,Prof-specialty,Wife,Black,Female,0,0,40,Cuba,<=50K
    response = client.post("/predict", json=data)
    #response = client.post("/predict", data=json.dumps(data))

    assert response.status_code == 200
    assert (response.json()["predict"][: len('Income <= 50k')]) == "Income <= 50k"
    #assert json.loads(response.text)[""] == "Income <= 50k"

def test_post_():
    data = {
        "age": 40,
        "workclass": "Private",
        "fnlgt": 193524,
        "education": "Doctorate",
        "education-num": 16,
        "marital-status": "Married-civ-spouse",
        "occupation": "Prof-specialty",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "capital-gain": 0,
        "capital-loss": 0,
        "hours-per-week": 60,
        "native-country": "United-States"
    }
        #40,Private,193524,Doctorate,16,Married-civ-spouse,Prof-specialty,Husband,White,Male,0,0,60,United-States,>50K
    response = client.post("/predict", data=json.dumps(data))

    assert response.status_code == 200
    assert (response.json()["predict"][: len('Income > 50k')]) == "Income > 50k"