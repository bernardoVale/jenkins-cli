FROM python:3.6-onbuild

ARG builder_home

RUN pip install --upgrade /usr/src/app

ENTRYPOINT ["/usr/local/bin/jenkins"]