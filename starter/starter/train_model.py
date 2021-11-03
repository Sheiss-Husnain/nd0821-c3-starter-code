from sklearn.model_selection import train_test_split

import pandas as pd

from ml.data import process_data

from ml.model import train_model

df = pd.read_csv("../data/census-clean.csv")

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(df, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

X_train, y_train, encoder, lb = process_data(train, categorical_features=cat_features, label="salary", training=True)

model = train_model(X_train,y_train)

pd.to_pickle(model,'../model/model.pkl')
pd.to_pickle(encoder,'../model/encoder.pkl')
pd.to_pickle(lb,'../model/lb.pkl')
