from os import getenv
from blog.model import Blog
from unittest import TestCase

BLOGAPI_TEST_ENGINE = getenv('BLOGAPI_TEST_ENGINE', 'sqlite:///:memory:')

class TestBlogAPI(TestCase):

    def setUp(self):
        self.blog = Blog(BLOGAPI_TEST_ENGINE)

    def tearDown(self):
        del self.blog

    def test_blog_query_property(self):
        """
        Test blog query property
        """
        assert isinstance(self.blog.query, object)
        assert hasattr(self.blog.query, 'all')
        assert callable(self.blog.query.all)


