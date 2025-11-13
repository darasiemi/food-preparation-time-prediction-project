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
