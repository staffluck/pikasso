# Pikasso

## Установка

```sh
git clone https://github.com/staffluck/pikasso.git
<venv> pip install -r requirements.txt
python manage.py migrate
python manage.py load_report_data
python manage.py runserver 5000
```

## Эндпоинты
```sh
[GET] /reports/ - Получение всех Report с Paginator по 20 страниц
[GET] /reports/test/ - Получение всех Report с Paginator по 20 страниц, немного другая реализация
```
