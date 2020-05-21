FROM python:3.6

MAINTAINER Gaby Tal "gabytal333@gmail.com"

#copy the module requirements
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["flaskapp.py"]
