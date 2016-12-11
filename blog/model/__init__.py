from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .store import Post

BLOGPOST_STORE_URI = getenv('BLOGPOST_STORE_URI', 'sqlite:///blog.db')


class Blog:
    """
    The Blog Application Interface

    :example:

    blog = Blog()
    blog.add(title='A new day', body='Today is a new day...')

    for post in blog.list():
        print 'Article titled "{}"'.format(post.title)
    """
    def __init__(self, uri=BLOGPOST_STORE_URI):
        """
        Constructs a BlogPost application object

        :param uri: URI for datastore, see SQLAlchemy documentation
        """
        self._engine = create_engine(uri)
        self._session = sessionmaker(self._engine)()

    @property
    def query(self):
        return self._session.query(Post)

    def add(self, title, body):
        """
        Add a new blog post

        :param title: Title of blog post
        :param body: The body of blog post

        :return: dict
        """
        o = Post(title=title, body=body)
        self._session.add(o)
        self._session.commit()
        return o.to_dict()

    def list(self):
        """
        List all blog posts

        :return: list() of dict()
        """
        return [o.to_dict() for o in self.query.all()]
