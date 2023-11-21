FROM python:3.7

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

COPY entrypoint.sh /code/entrypoint.sh

RUN chmod +x /code/entrypoint.sh

CMD ["/code/entrypoint.sh"]
