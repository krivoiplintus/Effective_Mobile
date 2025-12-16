FROM python:3.13.7-slim
WORKDIR /app/test
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY pytest.ini .
COPY test_config.ini .
COPY /test .
CMD ["pytest"]
