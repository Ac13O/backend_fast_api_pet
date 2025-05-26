# backend_fast_api_pet
venv creation (Windows):
- `python -m venv .venv`

venv activation(Windows):
- `.\\.venv\scripts\activate`

install fastapi
- `pip install "fastapi[standard]"`

install packages from requirements.txt:
- `pip install -r requirements.txt`

Starting server locally can be done one of two commands:
- `fastapi dev main.py`
- `uvicorn main:app`

Local server located on:
 http://127.0.0.1:8000

Local docs located on:
http://127.0.0.1:8000/docs
