FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY requirements/* .

RUN pip install -r prod.txt


COPY ./ /chatbot-test
WORKDIR /chatbot-test

ENV PYTHONPATH=/chatbot-test

RUN python main.py
EXPOSE 8888

