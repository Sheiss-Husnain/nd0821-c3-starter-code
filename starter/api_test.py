from main import app

from fastapi.testclient import TestClient
import json
client = TestClient(app)

def test_get():
    response = client.get("/")
    assert response.status_code == 200

def test_post():
    data = {
        "age": 37,
        "workclass": "Private",
        "fnlgt": 284582,
        "education": "Masters",
        "education-num": 14,
        "marital-status": "Married-civ-spouse",
        "occupation": "Exec-managerial",
        "relationship": "Wife",
        "race": "Black",
        "sex": "Female",
        "capital-gain": 0,
        "capital-loss": 0,
        "hours-per-week": 40,
        "native-country": "Cuba",
    }
  #  list = [(k, v) for k, v in data.items()]
        #37,Private,284582,Masters,14,Married-civ-spouse,Exec-managerial,Wife,White,Female,0,0,40,United-States,<=50K
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
    response = client.post("/predict", json=data)

    assert response.status_code == 200
    assert (response.json()["predict"][: len('Income > 50k')]) == "Income > 50k"
    #assert json.loads(response.text)["predict"] == "Income > 50k"