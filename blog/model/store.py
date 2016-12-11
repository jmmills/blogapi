# coding: utf-8
# generated using: sqlacodegen sqlite:///blog.db >blog/model/store.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


PostBase = declarative_base()
PostMeta = PostBase.metadata


class Post(PostBase):
    __tablename__ = 'posts'

    post_id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)

    def to_dict(self):
        return {'post_id': self.post_id, 'title': self.title,
                'body': self.body}

