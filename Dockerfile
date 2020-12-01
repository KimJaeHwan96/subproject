FROM python:3.7
RUN apt-get update && apt-get install -y

RUN mkdir -p /subproject
COPY . /subproject
RUN apt-get install -y nginx vim
RUN pip install -r /subproject/requirements.txt
RUN pip install gunicorn
WORKDIR /subproject

