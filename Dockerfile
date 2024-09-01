FROM python:3.12.3-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir

COPY . /app/


# Убедитесь, что настройки корректны
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]