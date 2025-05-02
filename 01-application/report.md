Команды, которые использовались для пуша образа в регистри:

# Переходим в папку проекта (где находятся app.py и Dockerfile)
cd /01-application

# Сборка образа
docker build -t selenesa/my-flask-app:v2 .

# Пушим в приватный репозиторий
docker push selenesa/my-flask-app:v2