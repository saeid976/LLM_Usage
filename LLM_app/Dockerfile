FROM python:3.10

RUN apt-get update
RUN apt-get -y install netbase

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["/usr/local/bin/python3.10", "/app/fastapi_runner.py"]
# CMD ["supervisord","-c","/app/supervisor/services.conf"]