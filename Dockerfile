FROM python:2.7.9
COPY ./requirements-dev.txt /usr/src/app/
COPY ./requirements.txt /usr/src/app/

RUN pip install -i http://pypi.douban.com/simple/ -r requirements-dev.txt \
	&& pip install -i http://pypi.douban.com/simple/ -r requirements.txt

COPY . /usr/src/app

CMD ["python","app.py"]