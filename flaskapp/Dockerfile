FROM python:3.10-slim
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt

ARG CONFIG_FILE=./config.py
COPY ${CONFIG_FILE} ./
COPY . .
CMD ["gunicorn","-w","4","--bind","0.0.0.0:5000","run:create_app()"]