# How to

## Build and Depliy Docker Environment
You need an account at hub.docker.com. Please go to the web page and create one, if you do not have one yet.

You'll need to install docker https://docs.docker.com/install/. Open a new terminal within the project directory and run:

1. Build the images: `docker-compose -f docker-compose-build.yaml build --parallel`
2. Push the images: `docker-compose -f docker-compose-build.yaml push`
3. Run the container: `docker-compose up`
