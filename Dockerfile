FROM python:3

RUN pip install pep8

ADD src /src
WORKDIR /src
