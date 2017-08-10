FROM python:3.5-slim
ADD . /code/
WORKDIR /code
# to activate alpine settings python:3.5-alpine
# RUN apk update && \
#    apk add --virtual build-deps gcc musl-dev && \
#    apk add postgresql-dev
RUN pip install -r requirements.txt
