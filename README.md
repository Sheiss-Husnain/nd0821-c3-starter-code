*  This project deploys a model using FastAPI.  Continuous Integration is achieved using GitHub Actions, Continuous Deployment is achieved using Heroku.
*  The placeholder dataset at the moment takes census data and classifies users by income level.
*  Data Version Control is achieved with dvc, and an AWS S3 bucket is used as the default remote.
*  Visit https://sheiss-census.herokuapp.com/docs to input a new data point and receive a prediction

*  Future updates will include front-end dev to host a neater form for end users which will be converted to json behind the scenes.

*  See the Actions tab to under the CI workflow.  Once a new commit is pushed to the repo, CI workflow is triggered and the new app will be automatically deployed via Heroku only if the checks are passed successfully.
