## Build
FROM python:3.8.5-alpine3.12

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY *.sh ./
COPY *.py ./
RUN pip install boto3 awscli

cmd python sentiment_analyzer.py
