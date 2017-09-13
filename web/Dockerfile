FROM python:3.6.1
MAINTAINER Patrick Kennedy <patkennedy79@gmail.com>
 
# Create the group and user to be used in this container
RUN groupadd django && useradd -m -g django -s /bin/bash django
 
# Create the working directory (and set it as the working directory)
RUN mkdir -p /home/django/app
WORKDIR /home/django/app
ADD . /home/django/app
 
# Install the package dependencies (this step is separated
# from copying all the source code to avoid having to
# re-install all python packages defined in requirements.txt
# whenever any source code change is made)
COPY requirements.txt /home/django/app
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the source code into the container
# COPY . /home/django/app
 
RUN chown -R django:django /home/django
 
USER django
