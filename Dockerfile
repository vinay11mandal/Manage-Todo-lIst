FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /tooList

COPY ./requirements.txt /
RUN apk update \
    && apk add bash \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
    && apk add postgresql \
    && apk del build-deps
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
