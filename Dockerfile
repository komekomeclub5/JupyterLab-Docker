FROM jupyter/datascience-notebook

RUN apt-get update
RUN pip install jupyterlab
RUN pip install pysimplegui



RUN jupyter serverextension enable --py jupyterlab
