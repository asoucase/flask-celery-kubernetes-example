# Dockerfile based on the latest Ubuntu Server LTS.
# Expected to move to Ubuntu Server 20.04 LTS soon.
FROM ubuntu:bionic

# Install python3.6 and pip
RUN apt update && apt install -y python3.6 python3-pip
# Install uwsgi through pip
RUN pip3 install uwsgi

# Create app folder
RUN mkdir -p /usr/share/app/
WORKDIR /usr/share/app/

# Create non-root user with limited capabilities and switch to it
RUN useradd --create-home appuser
RUN chown -R appuser:appuser .
USER appuser

# Copy requirements file and install packages
COPY flask_app/requirements.txt .
RUN pip3 install -r requirements.txt --user

# Copy application folder
COPY flask_app flask_app/
COPY wsgi.py .
COPY uwsgi.ini .

EXPOSE 9000

CMD ["/usr/local/bin/uwsgi", "--ini", "uwsgi.ini", "--die-on-term"]
