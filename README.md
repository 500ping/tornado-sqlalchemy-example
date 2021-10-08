# Intro
Basic todo app with tornado, sqlachemy and mysql.

## Setup Mysql
```
user: test
pass: test
db name: tornado_example
(*) change in db.py
```

## Installation
```
pip install -r requirements.txt
```

## Map tables
```
alembic revision --autogenerate -m "Add table"
alembic upgrade head
```

## Run project
```
python main.py
```
