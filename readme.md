# Simple Blog Django

Blog de prueba responsive que permite autenticacion con user o con cuenta de google. Creado con Django 3.2 y Python 3.8

## Dependencias

* Pillow
* Allauth
* Dajngo 3.2
* Tinymce

## Instalacion de dependencias

Desde la raiz del proyecto:

```
pip install -r requirements.txt
```

## Ejecutar proyecto

Creacion de la base de datos, tablas y migracion

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Cracion de usuario administrador

```
python manage.py createsuperuser
```

Ejecucion del proyecto

```
python manage.py runserver
```