FROM python:3.8-alpine

COPY . /app

WORKDIR /app
RUN apk add --upgrade \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

CMD ["python", "app.py"]
