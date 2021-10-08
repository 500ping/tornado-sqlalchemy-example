from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func

from db import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    status = Column(Boolean, default=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(BigInteger, ForeignKey('users.id'))