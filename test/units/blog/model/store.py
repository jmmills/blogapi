from os import getenv
from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from blog.model.store import Post, PostMeta

# Under special cases we may want overwrite what our connection URI is for
# testing example use case: testing our API against a different RDBMS
BLOGAPI_TEST_ENGINE = getenv('BLOGAPI_TEST_ENGINE', 'sqlite:///:memory:')
BLOGAPI_LOG_SQL = True if getenv('BLOGAPI_LOG_SQL',
                                 'false').lower() == 'true' else False


class TestPostStore(TestCase):
    """
    Tests our Post storage
    """
    def setUp(self):
        """
        Creates a test database before test methods run

        This method initializes an in-memory SQLite database of our Posts()
        SQLAlchemy model.

        :return: None
        """

        self.engine = create_engine(BLOGAPI_TEST_ENGINE, echo=BLOGAPI_LOG_SQL)
        self.session = sessionmaker(bind=self.engine)()

        PostMeta.create_all(self.engine)  # deploy schema to in-memory database

        return None

    def tearDown(self):
        """
        Drops the test database after each test method runs

        This method drops all in-memory tables, hands the session (back) back
        to the the engine, and closes down the engine.

        This processes is somewhat redundant when testing with an in-memory
        SQLite database, however if tests are run using a permanent RDBMS,
        being a good citizen here could save someone the grief of testing
        race-conditions.

        :return: None
        """

        PostMeta.drop_all(self.engine)  # drop all tables

        self.session.close()  # give session/connection back to connection pool
        self.engine.dispose()  # close all connections

        del self.session
        del self.engine

    def test_create(self):
        """
        Create and store a Post

        :return: None
        """
        a = Post(title='title', body='body')

        assert a.title == 'title'
        assert a.body == 'body'
        assert a.post_id is None, 'post is empty before commit'

        assert self.session.add(a) is None
        assert self.session.commit() is None

        assert isinstance(a.post_id, int), 'post commit post_id is int'

    def create_records(self, size=10):
        """
        Helper method to create test records

        :param size: how many test records to create, defaults to 10
        :return: None
        """
        for i in range(0, size):
            post = Post(title='title {}'.format(i), body='body {}'.format(i))
            self.session.add(post)

        self.session.commit()

    def test_read(self):
        """
        Test reading Posts from database

        :return:
        """
        self.create_records()

        a = self.session.query(Post).filter(Post.title == 'title 3')
        assert a.count() == 1
        a.first().body == 'body 3'

        b = self.session.query(Post).all()
        assert len(b) == 10
        assert isinstance(b[2], Post)
        assert b[2].title == 'title 2', b[2].title

    def test_update(self):
        """
        Test updating a record

        :return: None
        """
        self.create_records()

        q = self.session.query(Post).filter(Post.title == 'foo')
        assert q.first() is None
        assert q.count() == 0

        q = self.session.query(Post)
        assert q.count() == 10
        assert q.first() is not None

        q[1].title = 'foo'
        self.session.commit()

        q = self.session.query(Post).filter(Post.title == 'foo')
        assert q.first() is not None
        assert q.count() == 1

    def test_delete(self):
        """
        Test deleting a record

        :return: None
        """
        self.create_records()

        a = self.session.query(Post).filter(Post.title == 'title 5')
        a.first() is not None
        a.count() == 1

        a.delete()
        self.session.commit()

        q = self.session.query(Post)
        assert q.count() == 9
        assert len(q.all()) == 9

    def test_to_dict(self):
        """
        Tests Post().to_dict() method

        :return:
        """
        self.create_records()

        a = self.session.query(Post).first()
        d = a.to_dict()
        assert isinstance(d, dict)
