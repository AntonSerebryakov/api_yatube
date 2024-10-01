# API для Yatube 

 

Учебный проект Яндекс Практикум "API для Yatube". 

Представляет собой реализацию API для простого блога. 

 

## Установка 

 

1. Клонируйте репозиторий проекта: 

     

    ```bash 

    git clone git@github.com:AntonSerebryakov/api_final_yatube.git 

    ``` 

 

2. Перейдите в директорию проекта: 

     

    ```bash 

    cd api_final_yatube 

    ``` 

 

3. Установите виртуальное окружение: 

 

    ```bash 

    python -m venv venv  

    ``` 

 

4. Запустите виртуальное окружение: 

 

   ```bash 

   venv\Scripts\activate 

   ``` 

  

5. Установите зависимости: 

     

    ```bash 

    pip install -r .\requirements.txt   

    ``` 

 

6. Зайдите в поддиректорию yatube_api: 

    

    ```bash 

    cd yatube_api 

    ``` 

 

7. Создайте и примените миграции: 

 

    ```bash 

    python manage.py makemigrations 

    python manage.py migrate 

    ``` 

 

8. Запустите сервер: 

     

    ```bash 

    python manage.py runserver 

    ``` 

 

## Документация 

 

После запуска сервера по адресу [http://127.0.0.1:8000/redoc/] будет доступна документация для API Yatube. 

 

## Стек технологий 

 - Python 3.9 
- Django 

- Django REST Framework 

 

## Автор 

 

Проект создан [Антоном Серебряковым](https://github.com/AntonSerebryakov).  
