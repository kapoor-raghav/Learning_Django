# Installation and initial steps to configure Django
- Install uv - alternative to pip with faster speed (similar to bun in js)
- Create a virtual environment - uv venv (creates a folder named .venv)
- Activate the venv using - .\\.venv\Scripts\activate
- Installation - uv pip [package-name]

### Running Django Server
- **django-admin** startproject [project-name] (django-admin is provided once Django is installed by default).
- cd [project-name]
- python .\manage.py runserver [port-number](command to run the server).

## Manage.py
- Starting point of Django Code.

## Settings.py
- All the configurations are set here for project-level (extremely powerful).

## URL.py
- All the routing are set here.

## How are views created?

Create a new file called `views.py`

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World :)")
```

- view (Controller (where we write the logic)).
- eg request for accessing the homepage goes from views.py to urls.py


## How to configure paths in urls.py?
```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_us, name='contact'),
]
```

## Created folder for templetes and static

- Templetes for htms files
- Static for css files

## How to return HTML response from views?
- Define the HTML file at project/templates/website/index.html
- Go to settings.py and set the TEMPLATES directory
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Set template diretctory here
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- Import the render method from django.shortcuts
```python
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World :)")
    return render(request, template_name='website/index.html')
```
## How to include CSS?
- Create a new folder called static and add the style.css file
- Go to index.html file and add the following
```python
{% load static %}   <!-- required to be imported to load static elements -->
<head>
    <!-- static keyword is used to load static asset -->
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
```
- Then go to settings.py and add STATICFILES_DIRS setting
```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```
## Create Apps

- Create the app with the following command - python manage.- py startapp [app-name]
- Add the said app in settings.py
- Create a new folder for templates in chai App
- Inside the templates folder, create another folder with the same name as the project (here chai).
- Finally create a file called all_chai.html
- Create a view
- Then, copy the contents from urls.py and create a new urls.py in the chai folder.

## Solved problem of html dock type not loading ??
- press ctrl+, to access settings.
- search emmit.
- go to include languages item:-django-html  value:-html
- this to include html language suggestions in django template.

## How to use Layouts?
- Create a new file called layout.html in the templates folder under main project

```python
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        {% block title %}
        Default Value
        {% endblock title %}
    </title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
    <!-- static keyword is used to load static asset -->
</head>
<body>
    <nav>This is our navbar</nav>
    {% block content %}{% endblock content %}
</body>
</html>
```
- Then we can use the extends keyword to include the layout

## index.html
```python

{% extends "layout.html" %}

{% block title %}
Chai Aur Django
{% endblock title %}

{% block content %}
<h1>Chai aur Django | Homepage</h1>
    <h1><a href="about/">About Us</a></h1>
    <h1><a href="contact/">Contact Us</a></h1>
    <h1><a href="chai/">Chai</a></h1>
{% endblock content %}
```






