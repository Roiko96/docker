FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# התקנה דרך מראה מהיר
RUN pip install --no-cache-dir -r requirements.txt \
    --index-url https://pypi.org/simple \
    --timeout=100

COPY . .

CMD ["python", "app.py"]
