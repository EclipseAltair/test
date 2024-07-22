# Инструкция

> Для работы нужен python версии 3.11

1. Проверяем версию python и устанавливаем poetry
```bash
python --version  # Python 3.11.*
python -m pip install poetry
poetry --version  # Poetry (version *.*.*)
poetry install
```

2. Применяем миграции
```bash
.venv/bin/python manage.py makemigrations
.venv/bin/python manage.py migrate
```

3. Создаем суперпользователя админки
```bash
DJANGO_SUPERUSER_EMAIL=admin@admin.com DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_PASSWORD=admin123 .venv/bin/python manage.py createsuperuser --no-input
```

4. Запускаем сервер
```bash
.venv/bin/python manage.py runserver
```

5. Заходим в админку на сайт http://127.0.0.1:8000/admin
```bash
login: admin
password: admin123
```