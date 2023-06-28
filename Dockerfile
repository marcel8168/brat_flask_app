# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /flask_app

RUN mkdir /flask_app/brat
ADD https://github.com/nlplab/brat/archive/refs/heads/master.zip /tmp/brat-latest.zip
RUN unzip /tmp/brat-latest.zip -d /tmp/
RUN cp /tmp/brat-master/* /flask_app/brat -r

# Copy your Python code into the container
COPY . .

# Specify an empty command to keep the container running
CMD tail -f /dev/null