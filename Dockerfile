FROM python:3

MAINTAINER Jason Mills <jmmills@cpan.org>

RUN mkdir -pv /usr/src/app

WORKDIR /usr/src/app

ADD requirements.txt .
ADD requirements ./requirements

RUN pip install --no-cache-dir -r requirements.txt
