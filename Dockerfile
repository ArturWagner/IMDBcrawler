FROM python:2.7
ADD . /imdb
WORKDIR /imdb
RUN pip install -r requirements.txt