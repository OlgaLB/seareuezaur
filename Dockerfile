FROM python:3.7-slim

RUN apt-get -y update
RUN apt-get -y install mysql-server-*

RUN pip3 install flask
RUN pip3 install -U flask-cors
RUN pip3 install mysql-connector-python  
RUN pip3 install pytest
RUN pip3 install requests

RUN mkdir airports
WORKDIR /airports

RUN chmod 777 /airports
COPY main.py /airports
COPY api.py /airports
COPY populate.py /airports
ADD lib /airports/lib
ADD db /airports/db
ADD tests /airports/tests

RUN cd /airports

EXPOSE 5000

CMD python3 main.py & python3 api.py
