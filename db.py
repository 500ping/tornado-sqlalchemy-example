from tornado_sqlalchemy import SQLAlchemy

db_user = 'test'
db_password = 'test'
db_name = 'tornado_example'
database_url = f'mysql+pymysql://{db_user}:{db_password}@localhost/{db_name}'

db = SQLAlchemy(url=database_url)