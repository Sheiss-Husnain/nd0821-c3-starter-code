# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model is written by Sheiss Husnain, for the Udacity MLOps nanodegree.  It was written 11/3/21, using RandomForestClassifier.

## Intended Use

This model is part of a deployed FastAPI project.  It takes civilian census data as input and predicts whether their income is above or below $50k a year.

## Training Data

80% of the census-clean.csv dataset.

## Evaluation Data

20% of the census-clean.csv dataset.

## Metrics

Precision, Recall, fbeta scores.

## Ethical Considerations

No ethical considerations were made in the preliminary version.

## Caveats and Recommendations

Future versions of this model may account for racial bias if it is found to be apparent in version 1.

