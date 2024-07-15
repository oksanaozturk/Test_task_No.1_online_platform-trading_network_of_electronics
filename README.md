## Test_task_No.1_online_platform-trading_network_of_electronics

## Oнлайн платформа-торговой сети электроники

Проект предполагает реализацию следующего функционала:

- Авторизация и аутентификация пользователей.
- CRUD для моделей Networkobject и Product на сайте.
- Доступ к API имеют только активные сотрудники и Админы.
- Создание superuser.
- Добавлен admin action, очищающий задолженность перед поставщиком у выбранных объектов.
- Созданы инструкции для API в вариантах в swagger и redoc.
- Настройка фильтрации по странам (API)
- Настроены права доступа к API только для активных сотрудниов

### Используемые технологии:

 - Python
 - Django
 - PostgerSQL
 - Django REST framework
 - django-filter


<details>
<summary> Инструкция по развертыванию проекта</summary>


1) ### Для разворачивания проекта потребуется создать и заполнить файл .env  по шаблону файла env.sample

#### Добавьте секретный ключ Вашего проекта
SECRET_KEY=

#### Добавьте настройки для подключения к базе данных (ДБ должна быть создана)
 - POSTGRES_DB=
 - POSTGRES_USER=
 - POSTGRES_HOST=
 - POSTGRES_PORT=
 - POSTGRES_PASSWORD=

2) ### Используется виртуальное окружение - venv, зависимости записаны в файл requirements.txt
 - pip install -r requirements.txt

3) ### Перед запуском web-приложения создайте базу данных, создайте и примените миграции
 - python manage.py migrate

4) #### Используйте команду для создания суперпользователя.
 - python manage.py csu

5) #### Для загрузки данных из фикстур используйте команду
 - python manage.py loaddata fixtures.users.json
 - python manage.py loaddata fixtures.network.json

6) ### Команда для запуска Приложения: 
  - python manage.py runserver


</details>

### Автор проекта https://github.com/oksanaozturk