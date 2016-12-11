import hug
import blog

from unittest import TestCase


class TestRESTAPI(TestCase):
    def test_get_blog_list(self):
        """
        Test GETing blog list
        """
        resp = hug.test.get(blog, 'posts')
        assert resp.status == '200 OK'
        assert isinstance(resp.data, list)

    def test_create_blog_post(self):
        """
        Test POSTing to create post api
        """
        resp = hug.test.post(blog, 'post', { 'post_title': 'test', 'post_body': 'testing'})
        assert resp.status == '200 OK'
        assert isinstance(resp.data, dict)
        assert 'body' in resp.data
        assert 'title' in resp.data
        assert 'post_id' in resp.data

