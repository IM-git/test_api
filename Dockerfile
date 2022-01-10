FROM python:3.10

RUN mkdir -p /test_api/

WORKDIR /test_api/

COPY . /test_api/

RUN pip install --no-cache-dir -r requirements.txt

CMD pytest -s -v ./tests/ --alluredir=allureress