# Kittygram

[![Main Kittygram Workflow](https://github.com/igorKolomitseff/kittygram_final/actions/workflows/main.yml/badge.svg)](https://github.com/igorKolomitseff/kittygram_final/actions)

Kittygram - это платформа, позволяющая пользователям делиться фотографиями своих кошек.

## Функции проекта

* Регистрация и аутентификация пользователей.
* Возможность добавить кошек с указанием имени, даты рождения, фотографии и достижений.
* Просмотр кошек других пользователей и редактирование профилей своих кошек.

## Стек технологий
* Backend: 
  [Django](https://www.djangoproject.com/), 
  [Django REST Framework](https://www.django-rest-framework.org/), 
  [Gunicorn](https://gunicorn.org/)
* Frontend: 
  [NodeJS](https://nodejs.org/en), 
  [React](https://react.dev/)
* База данных: [PostgreSQL](https://www.postgresql.org/)
* Веб-сервер: [Nginx](https://nginx.org/)
* Контейнеризация: [Docker](https://www.docker.com/)

## Как развернуть проект
1. Клонируйте репозиторий и перейдите в директорию kittygram_final
```bash
git clone git@github.com:igorKolomitseff/kittygram_final.git
cd kittygram_final/
```

2. Создайте .env файл в корневой директории и заполните его данными в соответствии с файлом .env.example

3. Последовательно выполните приведённые ниже команды (если проект разворачивается на системе Linux, все последующие команды выполняются с использованием sudo)

```bash
docker compose -f docker-compose.production.yml up
docker compose -f docker-compose.production.yml exec backend python manage.py migrate
docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```

Откройте браузер и перейдите по адресу http://localhost:9000/ для доступа главной странице и http://localhost:9000/admin/ для доступа к административной панели.

### Автор

[Игорь Коломыцев](https://github.com/igorKolomitseff)