# coding: utf-8
# generated using: sqlacodegen sqlite:///blog.db >blog/model/store.py
from sqlalchemy import Column, Numeric
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Post(Base):
    __tablename__ = 'posts'

    post_id = Column(NullType, primary_key=True)
    title = Column(Numeric)
    body = Column(Numeric)
