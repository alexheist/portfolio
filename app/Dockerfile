FROM python:3.7-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEVENV=local

RUN apk update \
	&& apk add --virtual build-deps gcc python3-dev musl-dev g++ \
	&& apk add postgresql-dev \
	&& pip install psycopg2

RUN pip install --upgrade pip
COPY requirements/ /usr/src/app/requirements/
RUN pip install -r requirements/${DEVENV}.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
