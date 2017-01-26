FROM python:3.6

RUN mkdir /app
ADD . /app
WORKDIR /app
EXPOSE 8081

CMD ["python", "/app/cryptoquote.py"]
