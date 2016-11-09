FROM python:3.5
MAINTAINER Ville Koivunen <ville.koivunen@hel.fi>
RUN mkdir /respa
RUN apt-get update && apt-get install -y libgdal1h
WORKDIR /respa
ADD . /respa/
RUN mv docker-django-settings.py local_settings.py
RUN pip install -r requirements.txt
