FROM python:3.12-slim

WORKDIR /usr/app

COPY . /usr/app/

ENTRYPOINT [ "python", "main.py" ]