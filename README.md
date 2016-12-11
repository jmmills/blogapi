# blogapi

A Blog REST API

* [![Build Status](https://travis-ci.org/jmmills/blogapi.svg?branch=master)](https://travis-ci.org/jmmills/blogapi)
* [![Coverage Status](https://coveralls.io/repos/github/jmmills/blogapi/badge.svg?branch=master)](https://coveralls.io/github/jmmills/blogapi?branch=master)

## Deploy

Deploy directly from docker hub

    $ docker pull jmmills/blogapi
    $ docker run -d -p 8000:8000 jmmills/blogapi
    
## REST API Usage

* Get API Documentation

    ```
    $ curl -s http://localhost:8000 
    ```     
    
    ```json
    {
      "404": "The API call you tried to make was not defined. Here's a definition of the API to help you get going :)",
      "documentation": {
        "handlers": {
          "/posts": {
            "GET": {
              "usage": "Lists blog posts",
              "examples": [
                "http://localhost:8000/posts"
              ],
              "outputs": {
                "format": "JSON (Javascript Serialized Object Notation)",
                "content_type": "application/json"
              }
            }
          },
          "/post": {
            "POST": {
              "usage": "Adds a new blog post",
              "outputs": {
                "format": "JSON (Javascript Serialized Object Notation)",
                "content_type": "application/json"
              },
              "inputs": {
                "post_title": {
                  "type": "Basic text / string value"
                },
                "post_body": {
                  "type": "Basic text / string value"
                }
              }
            }
          }
        }
      }
    }
    ```
    
* Add a blog post

    ```
    $ curl -s -X POST 'http://localhost:8000/post?post_title=New&post_body=Post' 
    ```
    
    ```json
    {
        "post_id": 4,
        "title": "New",
        "body": "Post"
    }
    ```
      
* Get a list of posts

    ```
    $ curl -s -X GET http://localhost:8000/posts 
    ```
      
    ```json
    [
      {
        "post_id": 1,
        "title": "New",
        "body": "Post"
      },
      {
        "post_id": 2,
        "title": "New",
        "body": "Post"
      },
      {
        "post_id": 3,
        "title": "New",
        "body": "Post"
      },
      {
        "post_id": 4,
        "title": "New",
        "body": "Post"
      }
    ]
    ```

## Service Configuration

### Environment Variables

* BLOGPOST_STORE_URI: URI used to connect to data store, see [SQLAlchemy Documentation](http://docs.sqlalchemy.org/en/latest/core/engines.html)

## Developer Documentation

### System Requirements

* [Docker](https://docs.docker.com/engine/installation/)
* [Make](https://www.gnu.org/software/make/)
* [Python 3](https://www.python.org/downloads/)

### Install python development requirements

    $ pip install -r requirements/develop.txt
    
### Build 

    $ make
    
### Test

    $ make test
    
### Database schema helper script

    $ ./db.py 
    Usage: db.py [OPTIONS] COMMAND [ARGS]...

    Options:
      --uri TEXT  SQLAlchemy URI to deploy schema to
      --help      Show this message and exit.

    Commands:
      deploy  Deploys blog schema
      drop    Drops a blog schema

    
