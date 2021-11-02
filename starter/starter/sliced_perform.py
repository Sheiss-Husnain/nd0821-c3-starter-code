import pandas as pd

from ml.model import inference, compute_model_metrics

from ml.data import process_data

df = pd.read_csv(r"starter/data/census_clean.csv")

model = pd.read_pickle(r"starter/model/model.pkl")
encoder = pd.read_pickle(r"starter/model/encoder.pkl")
lb = pd.read_pickle(r"starter/model/lb.pkl")

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


def slice_perform(model, df, column, encoder, lb):

    file = open('{}_slice.txt'.format(column),'w')
    
    for value in df[column].unique():
        file.write(value)
        file.write('\n')

        df_temp = df[df[column]==value]

        X_test, y_test, encoder, lb = process_data(
            df_temp, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
        )

        y_pred = inference(model, X_test)

        precision, recall, fbeta = compute_model_metrics(y_test, y_pred)

        file.write('Precision   {}'.format(precision))
        file.write('Recall  {}'.format(recall))
        file.write('fbeta   {}'.format(fbeta))
        file.write('\n')
        file.write('-')
        file.write('\n')

if __name__ == "__main__":
    for cat in cat_features:
        slice_perform(model, df, cat, encoder, lb)