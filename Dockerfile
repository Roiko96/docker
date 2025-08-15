FROM python:3.12-slim

WORKDIR /app

# העתקה של הקבצים המקומיים
COPY . .

# התקנה מקומית (בלי חיבור ל־PyPI)
RUN pip install --no-cache-dir flask

CMD ["python", "app.py"]
