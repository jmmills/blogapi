from os import getenv
from blog.model import Blog
from blog.model.store import PostMeta
from unittest import TestCase

# TODO: make these proper unit tests by mocking sqlalchemy session
BLOGAPI_TEST_ENGINE = getenv('BLOGAPI_TEST_ENGINE', 'sqlite:///:memory:')


class TestBlogAPI(TestCase):

    def setUp(self):
        self.blog = Blog(BLOGAPI_TEST_ENGINE)
        PostMeta.create_all(self.blog._engine)

    def tearDown(self):
        PostMeta.drop_all(self.blog._engine)
        del self.blog

    def test_blog_query_property(self):
        """
        Test blog query property
        """
        assert isinstance(self.blog.query, object)
        assert hasattr(self.blog.query, 'all')
        assert callable(self.blog.query.all)

    def test_add_blog(self):
        """
        Test adding a blog entry via blog api
        """

        o = self.blog.add(title='test', body='ing')
        assert isinstance(o, dict)
        assert 'post_id' in o
        assert 'title' in o
        assert 'body' in o
        assert o['title'] == 'test'
        assert o['body'] == 'ing'

    def test_list_blogs(self):
        """
        Test getting a list of blogs via blog api
        """

        for i in range(0, 5):
            self.blog.add(title='test {}'.format(i), body='test {}'.format(i))

        l = self.blog.list()
        assert isinstance(l, list)

        for el in l:
            assert isinstance(el, dict)
            assert 'post_id' in el
            assert 'title' in el
            assert 'body' in el
