#!/bin/bash
set -e

# Ждём Postgres через Python
python - <<END
import os, time
import psycopg2
from psycopg2 import OperationalError

host = os.getenv("DATABASE_HOST", "postgres_db")
port = int(os.getenv("DATABASE_PORT", 5432))
user = os.getenv("DATABASE_USERNAME", "postgres")
password = os.getenv("DATABASE_PASSWORD", "1")
dbname = os.getenv("DATABASE_NAME", "ShopBoom")

while True:
    try:
        conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname=dbname)
        conn.close()
        print("Postgres is ready!")
        break
    except OperationalError:
        print("Waiting for Postgres...")
        time.sleep(2)
END

# Миграции
python manage.py migrate --noinput

# Создание суперпользователя
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-admin}
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-admin@example.com}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-admin123}

echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists() or \
User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" \
| python manage.py shell

# Запуск Django
exec python manage.py runserver 0.0.0.0:8000