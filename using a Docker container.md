
# Setup

## Install Docker

Follow [instructions](https://docs.docker.com/engine/installation/).

## Get needed sources

Clone locally a GitHub fork of <url>https://github.com/ragundez/PyData</url>.

## Build the Docker image

Browse to the root of the said local Git repository.

`docker build --pull -t facerec .`

Here, `facerec` is a tag for this docker image. Feel free to use whatever youn like.

# Operation

## Run the Docker image

`docker run -p 8888:8888 -p 6006:6006 -v ~/FaceRecRodrigoAgundez/PyData/:/notebooks -it --rm facerec`

Here `~/FaceRecRodrigoAgundez/PyData/` is the path to the local Git repository mentioned before.

## Test the installation

Browse in Jupyter to one of the notebooks and run the "import" cell.
