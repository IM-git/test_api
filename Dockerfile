FROM python:3.10

RUN mkdir -p /test_api/ &&  \
    mkdir /test_api/allureress

WORKDIR /test_api

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD pytest -s -v ./tests/ --alluredir=allureress
