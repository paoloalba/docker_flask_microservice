FROM python:3.7-slim

RUN pip install gunicorn
RUN pip install flask
# RUN pip install logging_tree

ADD /application /app

WORKDIR /app/

RUN mkdir -p logs

RUN chmod +x ./run.sh

ENTRYPOINT ["./run.sh"]