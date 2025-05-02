# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем зависимости
RUN pip install flask

# Устанавливаем переменную окружения для python
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в контейнер
COPY app.py .

# Открываем порт 8000
EXPOSE 8000

# Определяем переменную окружения AUTHOR
ENV AUTHOR="Александр Суслов"

# Запускаем приложение
CMD ["python", "app.py"]
