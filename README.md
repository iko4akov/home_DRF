# Deploy app to docker:
1. run postgreSQL:
    - load image postgres:
        - `docker pull postgresql:latest`
    - run postgres-container with name:`my_postgres`
        - `docker run --name my_postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres:latest`
    - connect for database(postgres in container):
        - `docker exec -it my_postgres psql -U postgres`
    - create database for work app, name = from `.env` import `DB_NAME` 
2. create image app with name `my_app_name`:
    - `docker build -t my_app .`
3. run docker container with name `my_app`:
    - `docker run -p 8080:80 my_app`
    - 
# Run project

- `clone repo`
- `change [.sample_env](.sample_env) for .env`
- `enter your data in .env`
- `sudo service postgresql start (if we have WSL)`
- `python3 manage.py migrate`
- `python3 manage.py csu`
- `python3 manage.py fill_users`
- `python3 manage.py fill`
run tests
~~~~coverage~~ run ~~--source='.' manage.py test~~~~


## Установка и запуск

Для установки приложения необходимо выполнить следующие шаги:

1. Клонировать репозиторий на свой компьютер:

git clone https://github.com/iko4akov/dj_practice.git

2. Установить зависимости:

`$pip install -r requirements.txt`

3. Создать файл .env:
    
`touch env.md`

4. В файле `.env` установить необходимые значения для корректной работы:
    - подключение к бд:
   
      `USER_PSQL=your_name`
      `PASS_PSQL=your_password`
      `DB_NAME=your_name_DB`
   
    - почта для рассылки сообщений:
      
       `EMAIL_HOST_USER=your_email`
       `EMAIL_HOST_PASSWORD=your_pass`

5. Проверьте состояние сервера PostgreSQL:
`service postgresql status`

6. Если служба не запущена, вы можете запустить ее с помощью:
`sudo service postgresql start`

7. Подключиться к БД(если вы на WSL2):
`psql -U your_name -h localhost`

8. Создать БД:
`CREATE DATABASE your_name;`

9. Запустить сервер:

`$python3 manage.py runserver` - for WSL
`python manage.py runserver` - for windows

10. Установить миграции:

`$python3 manage.py migrate`

11. Открыть браузер и перейти на страницу http://127.0.0.1:8000/

12. Запуск брокера:
`sudo service redis-server start`    
12. Наполнить БД:
`python3 manage.py fill`

## Функционал

Приложение предоставляет следующие активние страницы:

- http://127.0.0.1:8000/ - Главная страница приложения, на которой активна только одна вкладка __Контакты__
- http://127.0.0.1:8000/contact/ Страница с формой, на которой можно отправлять `POST` запросы с `email` и `password`


## Лицензия
Отсутствует=)

## Команды для использования fixture, с кодировкой `utf-8` на винде
`python -Xutf8 manage.py dumpdata catalog --indent 2 -o table.json`
`python -Xutf8 manage.py loaddata table.json`

отложенные задачи
celery -A config worker -l INFO

периожические
celery -A config beat -l INFO -s django

echo $(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')

