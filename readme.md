# Simple Blog Django

Blog de prueba responsive con django

## Dependencias

* Pillow
* Allauth
* Dajngo 4.0.3
* Tinymce

## Instalación de dependencias

Desde la raíz del proyecto:

```
pip install -r requirements.txt
```

## Ejecutar proyecto

Creación de la base de datos, tablas y migración

```python
python manage.py makemigrations blog
```

```python
python manage.py migrate
```

Creación de categorías

```python
python manage.py loaddata data.json
```

Cración de usuario administrador

```python
python manage.py createsuperuser
```

Ejecución del proyecto

```python
python manage.py runserver
```
