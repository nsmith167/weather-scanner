FROM python:3.11-slim

WORKDIR /weather-scanner
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "scanner.py"]