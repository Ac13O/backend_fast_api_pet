# Backend_fast_api_pet
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

## Database
In project used SQLite,
info of installing: [link](https://www.nic.ru/help/ustanovka-i-nastrojka-sqlite_11753.html?utm_source=google.com&utm_medium=organic&utm_campaign=google.com&utm_referrer=google.com#:~:text=%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F%3A%20%D0%BA%D0%B0%D0%BA%20%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C%20SQLite%20%2D%20%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%20SQLite%20%D0%BD%D0%B0%20Windows) 

To connect to db use command:

`sqlite3 <db name>`


To see info regarding table in db use command:

`PRAGMA table_info('<table_name>');`
