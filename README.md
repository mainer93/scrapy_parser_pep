# Проект парсинга pep с использованием Scrapy

Этот проект предназначен для парсинга документов PEP с официального сайта https://peps.python.org/ с использованием фреймворка Scrapy.
Задача — автоматизировать сбор информации о PEP-документах, включая номер, название, и статус.

## Установка и запуск

1. Клонировать репозиторий:

``` 
git clone git@github.com:mainer93/scrapy_parser_pep.git 
```

2. Перейти в папку проекта:

```
cd scrapy_parser_pep
```

3. Создать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/scripts/activate
```
4. Обновить pip:

```
python -m pip install --upgrade pip
```

5. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

6. Запустить парсер:

```
scrapy crawl pep
```

## Автор проекта

[Александр Заваленов](https://github.com/mainer93)