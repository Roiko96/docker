FROM python:3.12-slim

# תיקייה לעבודה
WORKDIR /app

# התקנת Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת הקוד
COPY . .

# הפעלת האפליקציה
CMD ["python", "app.py"]
