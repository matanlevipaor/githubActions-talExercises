# שלב 1: שימוש בתמונה בסיסית של Python
FROM python:3.9-slim

# שלב 2: הגדרת WORKDIR
WORKDIR /app

# שלב 3: העתקת קבצים
COPY requirements.txt requirements.txt
COPY flask.py flask.py

# שלב 4: התקנת תלויות
RUN pip install --no-cache-dir -r requirements.txt

# שלב 5: פתיחת פורט 5000
EXPOSE 5000

# שלב 6: הגדרת פקודת ההרצה
CMD ["python", "flask.py"]
