FROM python:2.7.9

COPY ./requirements.txt /usr/src/app/

RUN pip install -r requirements.txt
COPY . /usr/src/app

CMD ["python","app.py"]