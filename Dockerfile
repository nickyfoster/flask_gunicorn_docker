# Use the Python 3.7 image based on Alpine Linux as the base image
FROM python:3.7-alpine

# Set the working directory to '/application and copy files'
WORKDIR /application
ENV PYTHONPATH=/application
COPY requirements.txt requirements.txt
ADD project/ .

# Install the Python package in the working directory
RUN pip install -r requirements.txt --no-cache-dir
