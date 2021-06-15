# Практическое задание от MediaSoft: База фильмов
    Автор: Баданин Алексей
Для запуска проекта необходимы язык Python, фреймворк Django:
    
    sudo apt install python3.9

Если вы используете не встроенную БД SQLite, a PostgreSQL
необходимо установить:
    
    sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

Далее необходимо создать базу данных и пользователя для нее:

    sudo -u postgres psql
    CREATE DATABASE myproject;
    CREATE USER myprojectuser WITH PASSWORD 'password';
    ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
    ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myprojectuser SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
    \q

Далее создайте виртуальное окружение для проекта:

    sudo pip install virtualenv
    cd ~/myproject
    virtualenv myprojectenv

И активруйте:
        
    source myprojectenv/bin/activate

Далее установите зависимости из source requirements.txt

    pip install -r requirements.txt

Сделайте миграции:
    
    python manage.py makemigrations
    python manage.py migrate

Создайте супер-пользователя:

    python manage.py createsuperuser

Запустите сервер:

    python manage.py runserver

Для перехода в админ панель используйте урлу:

    http://127.0.0.1:8000/admin/


