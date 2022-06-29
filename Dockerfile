FROM python 3.8.3

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install netcat -y
RUN apt-get update -y && apt-get install postgresql gcc python3-dev musl-dev -y
RUN pip install --upgrade pip

COPY ./reg.txt .
RUN pip install -r req.txt

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT["/usr/src/app/entrypoint.sh"]

