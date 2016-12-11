FROM python:3

MAINTAINER Jason Mills <jmmills@cpan.org>

RUN mkdir -pv /usr/src/app

WORKDIR /usr/src/app

ADD requirements.txt .
ADD requirements ./requirements

RUN pip install --no-cache-dir -r requirements.txt

ADD blog ./blog
ADD test ./test

EXPOSE 8000

CMD uwsgi --http 0.0.0.0:8000 --module blog --callable __hug_wsgi__


