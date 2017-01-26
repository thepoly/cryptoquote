FROM python:3.6

RUN mkdir /app
ADD . /app
WORKDIR /app

CMD ["python", "/app/cryptoquote.py"]
