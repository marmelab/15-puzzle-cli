FROM python:3

ADD requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

ADD src /src
WORKDIR /src
