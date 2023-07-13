# Проект «API для Yatube»
## Описание
API для Yatub  является  социальной сетью в которой можно публиковать записи на любые темы, комментировать свои и чужие записи, подписываться на интересных авторов и следить за их обновлениями.
## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать, активировать и обновить виртуальное окружение:

```
python -m venv env
```
```
source venv/Scripts/activate
```
```
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
