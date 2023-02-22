### TEMPLATE DOCKERFDILE
# syntax=docker/dockerfile:1

# compiled conda
FROM continuumio/miniconda3


### add all dependencies ie. pip install requirements.txt
COPY requirements.txt requirements.txt
COPY env.yml env.yml

SHELL ["conda", "run", "-n", "main_env", "/bin/bash", "-c"]
### create a working directory
WORKDIR /working_dir


### either copy items from directory in order to be used in working dir
COPY /Latest /working_dir



# executing app
CMD [ "python3", "bin/main.py", "--host=0.0.0.0", ">>", "/working_dir/.debug.log","2>&1"]







