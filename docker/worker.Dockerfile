FROM ubuntu:bionic

RUN apt update && apt install -y python3 python3-pip

RUN mkdir -p /usr/share/app/
WORKDIR /usr/share/app/

COPY flask_app/requirements.txt .
RUN pip3 install -r requirements.txt

RUN pip3 install celery
COPY flask_app flask_app/
COPY worker.py .

CMD ["celery", "-A", "worker", "worker", "--loglevel=info"]
