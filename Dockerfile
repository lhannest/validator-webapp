FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y python3 python3-pip

RUN pip3 install eventlet configparser flask-socketio certifi urllib3

COPY /webapp/ home/webapp/

WORKDIR home

ENTRYPOINT ["python3", "-m", "webapp"]
