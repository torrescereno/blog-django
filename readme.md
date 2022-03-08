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

```python
python manage.py makemigrations
```

Creación de categoías

```python
python manage.py loaddata data.json
```

```python
python manage.py migrate
```

Cración de usuario administrador

```python
python manage.py createsuperuser
```

Ejecución del proyecto

```python
python manage.py runserver
```
