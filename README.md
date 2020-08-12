# Udacity Capstone
Udacity Capstone is a micro-service oriented text recognition software.

The project is split into two parts:
1. A Sentiments Analyser
2. A Entity Detector

At the moment, both use "AWS Comprehend" to process text. In a later version, I consider to write my own solution.

## Getting Started
### Prerequisite
Docker and Kubernetes are required.

## Configuration - docker
* rename set_env_template.sh to set_env.sh
* set the values for the environment as outlined in the bash script
* create a sns topic (which shall be also referred in the env variables)
* add a subscription to the topic (optional)
* call set_env.sh which also starts Docker
* copy file into the directory that are specified as landing zone
* wait for a mail.

## Configuration - kubernetes
* copy aws_secret_template.yaml to aws_secret.yaml
* Update aws_secret.yaml with your values
* call ./activate.sh

## Grading
In the folder grading, there is the following

### CI/CD, Github & Code Quality
* Screenshot Travis in directory screenshots
* README.md (including deployment)
* Deployment directions in directory deployment/readme.md

### Container
* Screenshot Docker images in hub in screenhsot folder
* Screenshot execution - local - in screenshot folder

## Deployment
* The project can be deployed to a kubernetes cluster
* Screenshot of multiple pods running are in screenshot folder

## Monitoring
* Screenshot The application is monitored by Amazon CloudWatch - see also code

# limitations
* various IO exceptions are not implemented (such as non existing directories) not implemented yet

# next development steps
1. extracting reporting code into another a single serviceservice
2. Adding loggers, explore ELK
3. writing a service that converts various documents into text
4. finding a solution for large texts
5. accepting streaming input
6. storing results into db
7. Add more analysis options
8. visualisation

This is currently not implemented, but will be in future versions of this application.