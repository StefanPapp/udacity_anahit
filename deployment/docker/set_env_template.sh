#!/bin/bash

export AWS_REGION=us-east-1
export AWS_ACCESS_KEY=your_access_key_here
export AWS_SECRET_KEY=your_secret_key_here
export LANDING_ZONE=/tmp/landing_zone
export COMPLETE_ZONE=/tmp/complete_zone
export ARN=here arn of sns topic

docker volume create --driver local \
    --opt type=none \
    --opt device=$LANDING_ZONE \
    --opt o=bind landing_zone

docker volume create --driver local \
    --opt type=none \
    --opt device=$COMPLETE_ZONE \
    --opt o=bind complete_zone

docker-compose up