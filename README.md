![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/Django-%23092E20.svg?style=flat&logo=django&logoColor=white)
![Django Rest Framework](https://img.shields.io/badge/Django%20Rest%20Framework-ff1709?style=flat&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)

# Мини проект «Курс доллара к рублю»

По запросу отображает актуальный курс доллара к рублю.

## Как запустить:

Клонируем себе репозиторий:

```
git@github.com:AnastasDan/currency_project.git
```

Переходим в директорию:

```
cd currency_project
```

Cоздаем и активируем виртуальное окружение:

* Если у вас Linux/MacOS:

    ```
    python3 -m venv venv
    ```

    ```
    source venv/bin/activate
    ```

* Если у вас Windows:

    ```
    python -m venv venv
    ```

    ```
    source venv/Scripts/activate
    ```

Устанавливаем зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```


Запускаем проект:

```
python manage.py runserver
```

Примечание: Если у вас нет Redis, закомментируйте строки с Redis в settings.py и раскомментируйте строки с локальным кэшем.

## После запуска переходим по этой ссылке:

http://127.0.0.1:8000/get_current_usd/