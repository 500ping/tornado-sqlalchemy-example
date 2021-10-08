# Intro
Basic todo app with tornado, sqlachemy and mysql.

## Setup Mysql
```
user: test
pass: test
db name: tornado_example
(*) change in db.py
```

## Map tables
```
alembic revision --autogenerate -m "Add table"
alembic upgrade head
```

## Installation
```
pip install -r requirements.txt
```

## Run project
```
python main.py
```