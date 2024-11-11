# Используем официальный Python образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл requirements.txt в контейнер и устанавливаем зависимости
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта в контейнер
COPY . .

# Устанавливаем переменную окружения для Django
ENV DJANGO_SETTINGS_MODULE=server.settings.production

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Определяем команду по умолчанию для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]