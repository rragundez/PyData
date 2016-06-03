
# Building the Docker image

`docker build --pull -t facerec .`

# Running the Docker image

`docker run -p 8888:8888 -p 6006:6006 -v ~/FaceRecRodrigoAgundez/PyData/:/notebooks -it --rm facerec`

Here `~/FaceRecRodrigoAgundez/PyData/` is the path to a local Git repository. Said repository is cloned from a GitHub fork of <url>https://github.com/ragundez/PyData</url>.
