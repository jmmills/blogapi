import hug

from .model import Blog

"""
The Blog API
"""

blog = Blog()


@hug.get('/posts')
def list_posts():
    """Lists blog posts"""
    return blog.list()


@hug.post('/post')
def add_post(post_title: hug.types.text, post_body=None):
    """Adds a new blog post"""
    return blog.add(title=post_title, body=post_body)

