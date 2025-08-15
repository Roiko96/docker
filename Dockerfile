FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# התקנת תלויות
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# קבצי הפרויקט
COPY . .
RUN chmod +x entrypoint.sh

# פורט ה-Web
EXPOSE 5000

# כניסה מאוחדת — ברירת מחדל CLI (תואם למה שעבד לך)
ENTRYPOINT ["./entrypoint.sh"]
CMD ["cli"]
