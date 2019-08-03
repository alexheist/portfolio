FROM python:3.7-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEVENV=production

COPY requirements.txt /usr/src/app/requirements.txt

RUN apk update \
	&& apk add --virtual build-deps gcc python3-dev musl-dev g++ \
	&& apk add postgresql-dev \
	&& pip install psycopg2 \
	&& apk add libffi-dev \
        && pip install --upgrade pip \
        && pip install -r requirements.txt

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/scripts/entrypoint.prod.sh"]
