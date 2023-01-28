### TEMPLATE DOCKERFDILE
# syntax=docker/dockerfile:1

### compile python as a package to be used
FROM python:3.8-slim-buster


### add all dependencies ie. pip install requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

### create a working directory
WORKDIR /working_dir


### either copy items from directory in order to be used in working dir
COPY /Latest /working_dir


# executing app
CMD [ "python3", "./bin/main.py", "--host=0.0.0.0"]







