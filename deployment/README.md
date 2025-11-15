# Deployment
## Web Service API
To install fastapi uvicorn
```bash
pip install fastapi uvicorn
```
To install uv
```bash
pip install uv
```
To initialize uv
```bash
uv init
```
We don't need main.py, so remove it
```bash
rm main.py
```
To add modules
```bash
uv add scikit-learn fastapi uvicorn pandas numpy
```
We also have a development dependency we won't need in production
```bash
uv add --dev requests
```

To run a specific script e.g train.py in deployment folder
```bash
uv run python -m deployment.train
```

To run the fastapi web app
```bash
uv run uvicorn deployment.predict:app --host 0.0.0.0 --port 9696 --reload
```

To run our test
```bash
uv run python -m deployment.test
```
## Best Practices
To install black and isort for code formating
```bash
uv add --dev black isort pre-commit
```

To run the formatting
```bash
uv run black .
```
```bash
uv run isort .
```

To install precommit hooks
```bash
uv run pre-commit install
```
To run precommits
```bash
uv run pre-commit run --all-files
```
Everytime you make changes to the code and make a commit, you see something similar to this which runs black and isort checks on the code
![Precommit](../images/precommits.jpeg)
## Docker
To build docker image
```bash
docker build -t food-prep .
```

To run the container
```bash
docker run -it --rm -p 9696:9696 food-prep
```

Again, to run the test to ensure the web service endpoint is up and running, 
```bash
uv run python -m deployment.test
```
## Cloud Deployment
I used AWS Elasticbeanstalk for cloud deployment
```bash
uv add --dev awsebcli
```
To initialize the EB environment:
```bash
uv run eb init -p docker -r eu-north-1 food-prep
```
This command configures the EB environment with the following parameters:

- -p docker: Specifies the platform as Docker.
- -r eu-north-1: Sets the region to eu-north-1. You can choose a different region based on your account information.
- food-prep: Defines the name of the environment.

To show the platform, run
```bash
uv run eb platform show
```
To create EB environment and deploy model
```bash
uv run eb create food-prep-env
```
You will have to have EB permissions to make this work

Again, to run the test to ensure the web service endpoint is up and running, this time the host has been changed to the cloud endppint
```bash
uv run python -m deployment.test
```
You will see
![Response of call to endpoint](../images/sample_test.jpeg)

When you check the endpoint created by AWS, you will see
You will see
![Fast API docs](../images/fast_api_docs.jpeg)

And the response looks like,
You will see
![Fast API docs](../images/fast_api_response.jpeg)

To terminate
```bash
uv run eb terminate food-prep-env
```
