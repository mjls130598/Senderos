FROM python:3.7-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN apk add gcc python3-dev jpeg-dev zlib-dev musl-dev
RUN pip install -r requirements.txt