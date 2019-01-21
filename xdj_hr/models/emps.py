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
