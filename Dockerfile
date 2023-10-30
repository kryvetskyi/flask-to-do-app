FROM python:3.11.6-slim-bullseye
LABEL authors="kryvetskyi"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN flake8 .
RUN pytest tests

ENTRYPOINT ["gunicorn", "-w 2", "-b 0.0.0.0:5002", "app:app"]
