# Simple Blog Django

Blog de prueba responsive que permite autenticación con user o con cuenta de google. Creado con Django 3.2 y Python 3.8

## Dependencias

* Pillow
* Allauth
* Dajngo 3.2
* Tinymce

## Instalación de dependencias

Desde la raíz del proyecto:

```
pip install -r requirements.txt
```

## Ejecutar proyecto

Creación de la base de datos, tablas y migración

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Cración de usuario administrador

```
python manage.py createsuperuser
```

Ejecución del proyecto

```
python manage.py runserver
```