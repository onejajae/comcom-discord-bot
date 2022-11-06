FROM python:3.9
WORKDIR /bot

ADD . .
RUN pip install -r ./requirements.txt

ENV PYTHONUNBUFFERED=0

ENTRYPOINT [ "python", "main.py" ]