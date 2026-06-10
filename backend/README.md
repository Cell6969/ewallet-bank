# Backend for E-wallet Bank

## Setup Fast API
make sure you already setup your environment and install dependency

```sh
pip install -r requirements.txt
```

## Run Development
Using Uvicorn
```sh
uvicorn app.main:app --reload
```

## Run Production
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```