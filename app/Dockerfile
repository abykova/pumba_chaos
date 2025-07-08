FROM python:3.10-slim

WORKDIR /app
COPY main.py .

RUN pip install flask redis

CMD ["python", "main.py"]
