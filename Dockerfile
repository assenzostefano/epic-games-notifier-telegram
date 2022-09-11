FROM python:3.10-alpine

ENV BOT_TOKEN 0

RUN mkdir -p /app

VOLUME [ "/app/data" ]

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]