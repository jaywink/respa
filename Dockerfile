FROM python:3.5
MAINTAINER Ville Koivunen <ville.koivunen@hel.fi>
RUN mkdir /code
RUN apt-get update && apt-get install -y libgdal1h
ADD . /code/
WORKDIR /code
RUN mv docker-django-settings.py local_settings.py
RUN pip install -r requirements.txt
