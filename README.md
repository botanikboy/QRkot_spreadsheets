# API сервис для краудфандинга и помощи котам QRKot.
Приложение для Благотворительного фонда для котиков с возможностью создания целевых проектов и открытого финансирования через пожетвования пользователей.

## Инструкция по запуску
Для запуска произведите действия ниже.
Клонировать репозиторий и перейти в него в командной строке:

```
git clone 

cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3.8 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

В корне проекта создайте .env файл.
Формат .env файла (смотри [.env.example](.env.example))
Для получения данных Google API от своего аккаунта воспользуйтесь инструкцией:
https://cloud.google.com/iam/docs/keys-create-delete

Для старта сервера из корневой директории проекта введите команду:
```
uvicorn app.main:app
```

Описание запросов и доступных эндпоинтов можно посмотреть по адресу после запуска проекта: http://127.0.0.1:8000/docs

## Основные технологии
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/latest/)

## Об авторе
Разработано:
[Илья Савинкин](https://www.linkedin.com/in/ilya-savinkin-6002a711/)
