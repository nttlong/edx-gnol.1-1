import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Emps(Base):
    __tablename__ = 'emps'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    first_name = Column(String)
    last_name = Column(String)

import xdj_sql

from django.db import models

@xdj_sql.table("emps")
class Emps(xdj_sql.models.Base):
    code = xdj_sql.fields.text(max_len=45)
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
