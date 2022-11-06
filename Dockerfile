FROM python:3.9
WORKDIR /bot

ADD . .
RUN pip install -r ./requirements.txt

ENTRYPOINT [ "python", "main.py" ]