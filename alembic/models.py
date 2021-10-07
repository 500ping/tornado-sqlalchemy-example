from sqlalchemy import Column, BigInteger, String, Boolean
from db import db 


class Task(db.Model):
    __tablename__ = 'tasks'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    status = Column(Boolean)

