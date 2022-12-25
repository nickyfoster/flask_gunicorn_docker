FROM python:3.7-alpine

WORKDIR /application
ENV PYTHONPATH=/application

COPY project/setup.py setup.py
RUN pip install .