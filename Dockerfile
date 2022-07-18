FROM python:3.7.5-slim-buster
LABEL ExtraLime <willdox7@live.com>

RUN apt-get update && apt-get install

ENV INSTALL_PATH /wdys
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
# RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "wdys.app:create_app()"