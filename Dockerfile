FROM python:3.11

WORKDIR /app
COPY backend /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["python", "app/loop_worker.py"]
