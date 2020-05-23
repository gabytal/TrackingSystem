FROM python:3.6

MAINTAINER Gaby Tal "gabytal333@gmail.com"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "flaskapp.py"]
