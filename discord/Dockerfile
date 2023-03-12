### TEMPLATE DOCKERFDILE
# syntax=docker/dockerfile:1

# compiled conda
FROM continuumio/miniconda3


### add all dependencies ie. pip install requirements.txt
COPY /Latest /Latest
COPY requirements.txt requirements.txt
COPY env.yml env.yml
RUN conda env create -f env.yml -n main_env
# RUN conda activate main_env

# Override default shell and use bash
SHELL ["conda", "run", "-n", "main_env", "/bin/bash", "-c"]

# RUN conda env list
### create a working directory
# SHELL ["conda","list","|" , "grep", "boto3" ]

### either copy items from directory in order to be used in working dir
# COPY /Latest /working_dir

# Demonstrate the environment is activated:
# RUN echo "Make sure boto3 is installed:"
# RUN python -c "import boto3"


# Python program to run in the container
COPY /Latest/bin/main.py /Latest/bin/main.py
ENTRYPOINT ["conda", "run", "-n", "main_env", "python", "/Latest/bin/main.py"]

# # executing app
# CMD [ "python3", "bin/main.py", "--host=0.0.0.0", ">>", "/working_dir/.debug.log","2>&1"]







