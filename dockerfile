FROM python:3.13-slim
WORKDIR /usr/src/loglens

COPY . .

ENTRYPOINT ["python","loglens.py"]