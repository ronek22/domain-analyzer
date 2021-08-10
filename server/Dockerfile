FROM python:3.9.5-slim-buster

WORKDIR /code

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["/code/entrypoint.sh"]

CMD ["flask", "run", "--host", "0.0.0.0"]
