# Beispiel-Dockerfile für das integrierte System
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "src/api/main_api:app", "--host", "0.0.0.0", "--port", "8000"]
