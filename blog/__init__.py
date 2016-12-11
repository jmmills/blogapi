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
def add_post(title: hug.types.text, body: hug.types.text):
    """Adds a new blog post"""
    return blog.add(title=title, body=body)

