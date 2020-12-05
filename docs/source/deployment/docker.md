# Docker FAQ

## Common commands
```bash
# List available images
sudo docker images

# List running containers
sudo docker container ls

# Build docker image from a dockerfile in the current directory
sudo docker build --tag image_name:image_tag .

# Remove all images
docker image prune -a
or
docker rmi -f $(docker images -a -q)

# Acess a bash shell within a running container
sudo docker run --rm -it 6c8bbe6e0ffe /bin/bash

# Echo output when running docker build
RUN echo $(mpirun --version)
RUN echo $(ls ~)
RUN echo $($PATH)
```

## [Activating a Conda environment in your Dockerfile](https://pythonspeed.com/articles/activate-conda-dockerfile/)
```docker
# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
```

## [Tips to Reduce Docker Image Sizes](https://hackernoon.com/tips-to-reduce-docker-image-sizes-876095da3b34)

## [Create Docker Images for Docker Hub](https://www.pluralsight.com/guides/create-docker-images-docker-hub)

## [Debugging applications with totalview in dockers](https://totalview.io/blog/how-debug-c-applications-docker-container)