#!/bin/bash

export DOCKER_NAME=sa
export ACC_KEY=
export SEC_KEY=
export REGION=us-east-1

docker exec $DOCKER_NAME aws configure set aws_access_key_id $ACC_KEY
docker exec $DOCKER_NAME aws configure set aws_secret_access_key $SEC_KEY
docker exec $DOCKER_NAME aws configure set default.region $REGION