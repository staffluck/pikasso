# Pikasso

## Установка

```sh
git clone https://github.com/staffluck/pikasso.git
<venv> pip install -r requirements.txt
python manage.py migrate
< Скачать и положить файл-импорт в корень проекта >
python manage.py load_report_data <название файла>
python manage.py runserver 5000
```

## Эндпоинты
```sh
[GET] /reports/ - Получение всех Report с Paginator по 20 страниц
[GET] /reports/test/ - Получение всех Report с Paginator по 20 страниц, немного другая реализация
```
