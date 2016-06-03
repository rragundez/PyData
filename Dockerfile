FROM gcr.io/tensorflow/tensorflow:latest
MAINTAINER Asaf Elron <asaf.elron@gmail.com>
RUN pip install scikit-learn
RUN apt-get update
RUN apt-get --yes install libopencv-dev python-opencv
RUN rm -rf /notebooks/*
ADD *.ipynb /notebooks/
WORKDIR /notebooks
CMD ["/run_jupyter.sh"]
