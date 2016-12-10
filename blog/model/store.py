# coding: utf-8
# generated using: sqlacodegen sqlite:///blog.db >blog/model/store.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Post(Base):
    __tablename__ = 'posts'

    post_id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
