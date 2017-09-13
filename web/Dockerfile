FROM python:3.6.1
MAINTAINER Patrick Kennedy <patkennedy79@gmail.com>
 
# Create the group and user to be used in this container
RUN groupadd django && useradd -m -g django -s /bin/bash django
 
# Create the working directory (and set it as the working directory)
RUN mkdir -p /home/django/
WORKDIR /home/django/

ADD . /home/django/

RUN pip install --no-cache-dir -r /home/django/requirements.txt
 
# Copy the source code into the container
# COPY . /home/django/app
 

RUN ls -la /home/django/
RUN find /home/django/
