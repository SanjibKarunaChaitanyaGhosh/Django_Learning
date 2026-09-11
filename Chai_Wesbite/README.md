## first step 

create views.py

```bash
from django.http import HttpResponse 
```
HttpResponse is a class provided by Django.

It creates an HTTP response that is sent back to the user's browser.

# When a browser requests a page, Django expects a response, and HttpResponse is the simplest one.


```bash
def home(request):
    return HttpResponse("Hello, World. You are at Chai website")
```
This is called a Function-Based View (FBV).

A view is simply a Python function that:

Receives an HTTP request.
Processes it (if needed).
Returns an HTTP response.

Browser
    │
    ▼
Request
    │
    ▼
home(request)   ← View
    │
    ▼
HttpResponse("Hello, World...")
    │
    ▼
Browser displays the text

# request → An HttpRequest object containing information about the incoming request.

Example information inside request:

URL
HTTP method (GET, POST)
User
Cookies
Session
Form data

Even if you don't use it yet, Django always passes the request object.

```bash
return HttpResponse("Hello, World. You are at Chai website")
```

return sends an HTTP response back to the browser.

If you visit:
http://127.0.0.1:8000/

The browser receives:
Hello, World. You are at Chai website

User types URL
       │
       ▼
urls.py
       │
       ▼
views.py
       │
       ▼
Model (optional)
       │
       ▼
Template (optional)
       │
       ▼
Response to browser


Why is it called a "view"?

In the Model–View–Template (MVT) architecture:

Model → Handles data (database)
View → Handles business logic and decides what response to return
Template → Defines what the user sees (HTML)

So a view is the component that receives the request and decides what the user gets back.

## urls.py

Think of urls.py as the traffic controller of your website.

Whenever a user visits a URL, Django checks urls.py to decide which function (view) should handle that request.

```bash
from django.contrib import admin
```
What does this do?

This imports Django's built-in admin panel.

admin contains the admin website that Django provides.

```bash
from django.urls import path
```
What does this do?

It imports the path() function.

path() is used to create URL routes.

```bash
path(URL, View, Name)
```

```bash
from . import views
```

The dot (.) means

"Import from the current folder."

Suppose your project looks like this:
```bash
FirstAPP/
    views.py
    urls.py
    models.py
```

Import the views.py file from this same app.

```bash
Now Django can use
```
```bash
views.home
views.about
views.contact
```

```bash
urlpatterns = [
```

This is simply a Python list.

Inside this list, we define all the URLs of the project/app.

Django reads this list from top to bottom.

## First URL path("admin/", admin.site.urls), Meaning
If someone visits http://127.0.0.1:8000/admin/

Django opens the admin panel.
```bash
Browser
   │
   ▼
/admin/
   │
   ▼
admin.site.urls
   │
   ▼
Django Admin Panel
```

## What is name=?

This is a name given to the URL.

Instead of writing URLs directly in templates, Django recommends using these names.

| URL entered in browser | Django matches | View function called | Output          |
| ---------------------- | -------------- | -------------------- | --------------- |
| `/`                    | `''`           | `home()`             | Home page       |
| `/about/`              | `'about/'`     | `about()`            | About page      |
| `/contact/`            | `'contact/'`   | `contact()`          | Contact page    |
| `/admin/`              | `'admin/'`     | Django Admin         | Admin dashboard |


User types URL
       │
       ▼
    Browser
       │
       ▼
    urls.py
       │
       ▼
Find matching path()
       │
       ▼
Call corresponding view
       │
       ▼
    views.py
       │
       ▼
Generate Response
       │
       ▼
Browser displays page

# For example, if the user visits:
```bash
http://127.0.0.1:8000/about/
```
    Browser
       │
       ▼
    urls.py
       │
       ▼
path('about/', views.about)
       │
       ▼
views.about(request)
       │
       ▼
HttpResponse("Hello, World. You are at Chai website")
       │
       ▼
    Browser

```bash
URL → View → Template → Response
```

## 1. What are Templates?

A template is an HTML file that Django uses to generate web pages.

Instead of sending plain text like:
```bash
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")
```
### Django can send an HTML page:
```bash
Browser
   ↑
   |
Django View
   |
Template (home.html)
```

### Example
```bash
# views.py

from django.shortcuts import render

def home(request):
    return render(request, "home.html")
```
### When someone vists our website

```bash
Request
   ↓
views.py
   ↓
home.html (Template)
   ↓
Browser shows the webpage
```

### 2. What is the Static Folder?

The static folder stores files that don't change when the page is requested.
These files are called static files because Django serves them as-is.

# Example Project Structure


MyProject/

│
|__ MyProject/
|
├── templates/
│      home.html
│      about.html
│
├── static/
│      css/
│          style.css
│
│      images/
│          logo.png
│
│      js/
│          app.js
│
├── views.pSpecialy
├── urls.py
└── settings.py

### 1. TEMPLATES setting in settings.py

```bash
TEMPLATES = [
    {
        "DIRS": ['templates'],
    }
]
```Special

# What is "DIRS"?

DIRS tells Django where to look for HTML template files.

## This imports Django's helper function called render().

```bash
from django.shortcuts import render
```

```bash
render(request, template_name, context)
```

request → the user's HTTP request
template_name → HTML file to display
context → data to send to the template (optional)


    Browser
        │
        ▼
    urls.py
        │
        ▼
    home(request)
        │
        ▼
    render(request, "index.html")
        │
        ▼
    templates/index.html
        │
        ▼
    HTML sent back to browser

### load
## index.html
```bash
{% load static %}

<link rel="stylesheet" href="{% static 'css/style.css' %}">
```
# settings.py
```bash
import os
```
```bash
STATIC_URL = "static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

or (recommended in modern Django):

```bash
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```
# Django template that loads a CSS file from the static folder.


## Key Concepts Learned

* Modern Python package management using **uv**
* Virtual environment creation
* Django project setup
* Running the development server
* Django template rendering
* Static file management
* Linux networking commands for debugging
* Understanding the difference between **Templates** and **Static Files**


## Django Documentation
https://docs.djangoproject.com/en/6.0/topics/templates/

## Django Templates
https://docs.djangoproject.com/en/6.0/topics/templates/

## How to make an APP within Django ?
* 1. have to check manage.py is there or not after "ls" command
* 2. python manage.py startapp <app name>
* 3. you have to aware your main project about new app
```bash
INSTALLED_APPS = [
    "chai",
]
```
* 4. now your app is properly installed
* 5. within newAPP I create templates/chai/all_chai.html
* 6. for suggestion follow point 7
* 7. ctrl+ ---> type emmet --> include langage --> item ==> django-html and value ==> html
* 8. make an urls.py file within app and copy all from main urls.py
* 9. transfer control of the new urls.py to the main urls.py
```bash
from django.urls import path, include
urlpatterns = [
    path('chai/',include('chai.urls')),
]
```
* 10. within main templates creat a file layout.html
```bash
<body>
    type block_unnamed and press enter
    this block can easily overwrite
    {% block  content%}{% endblock %}
</body>
```

### layout
* this is default template, we write it only once
* no need of any predefine temple in html which given by default, so delete that
* {% extends "layout.html" %} within index.html
* we can also extends this within APP

## Installing TailwindCSS

https://pypi.org/project/django-tailwind/

```bash
uv pip install django-tailwind
```
## hot-reload
```bash
uv pip install "django-tailwind[reload]"
```

## if output look like this "Audited 1 package in 2ms" then install pip

* https://pip.pypa.io/en/stable/installation/

```bash
https://pip.pypa.io/en/stable/installation/
```

```bash
python -m ensurepip --upgrade
```
* or,
```bash
python -m pip install --upgrade

```
## hot-reload using pip
```bash
pip install "django-tailwind[reload]"
```

## upgrade pip if needed
```bash
python -m pip install --upgrade pip
```

## Verify your installation
```bash
python --version
python -m pip --version
which python
which pip
```

# go to the main app, within main project settings.py
```bash
INSTALLED_APPS = [
    "chai",
    "tailwind",
]
```

# go to mian Project and ls if you can see manage.py
```bash
python manage.py tailwind init
```

Enter Tailwind app name [theme]: 
Choose template:
1 - Tailwind v4 Standalone - Simple and doesn't require Node.js
2 - Tailwind v4 Full - All the bells and whistles, requires Node.js
3 - Tailwind v3 Full - Legacy template for Tailwind v3 projects, requires Node.js
Enter choice [1-3]: 1

# go to the main app, within main project settings.py
```bash
INSTALLED_APPS = [
    "chai",
    "tailwind",
    'theme',
]
```

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS=['']

## to find Internal IP you can use the below command
```bash
hostname -I
``` 
or, 

```bash
ip route get 1.1.1.1
```
192.168.x.x → Your local (internal) IP on your Wi-Fi or Ethernet network.

## now we have to INSTALL tailwind using manage.py
```bash
python manage.py tailwind install
```
## added these two lines in layout.html
```bash
{% load static tailwind_tags %}
{% tailwind_css %}
 ```

# In the give position as mentioned below

{% load static tailwind_tags %}
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        {% block title %}Special Chai{% endblock %}
    </title>

    <link rel="stylesheet" href="{% static 'css/style.css' %}">
     {% tailwind_css %}
</head>


## tailwind still not connected although you can write tailwind in layout.html
* first you have to go the new terminal, go to the your project then run the below comment
```bash
 python manage.py tailwind start
 ```

 ## if you install tailwind using node.js, you have to add this within settings.py

```bash
which npm
```

 ```bash
 NPM_BIN_PATH='/home/sanjib/.nvm/versions/node/v22.21.0/bin/npm'
 ```

 ## for windows user 
 ```bash
 NPM_BIN_PATH=r"C:\Program File\etc\etc"
 ```

 ## in settings.py for relaod tailwind automatically
 ```bash
 INSTALLED_APPS = [
    ------------------------------
    ------------------------------
    "django_browser_reload"
]
```
# and

```bash
MIDDLEWARE = [
    ----------------------------------------------------------
    -------------------------------------------------------------
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
```
# and go to the urls.py
```bash
urlpatterns = [
    ---------------------------------------
    ----------------------------------------------

    path("__reload__/",include("django_browser_reload.urls"))
]
```

## RESTART YOU SERVER
```bash
python manage.py runserver 8001
python manage.py tailwind start
```

### ADMIN panel stated here

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

```bash
python manage.py migrate
```
# restart server again, no error
you can go to the admin page

```bash
http://127.0.0.1:8001/admin/login/?next=/admin/
```

# Create Super User
```bash
python manage.py createsuperuser
```

## reset django admin password

```bash
python manage.py changepassword <your_username>
```

## go to the APP/modles.py
```bash
from django.db import models
from django.utils import timezone
```

# Create your models here.
```bash
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KI','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=CHAI_TYPE_CHOICE)

    def __str__(self): # it effects the name iwqithin admin panel
        return self.name
```

```bash
pip install Pillow
```

## settings.py
```bash
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
```

## URLS.PY in main project

```bash
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [-----
                    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```

# Django don't know that you have create the model, SO -->
## you have to do migration for that
```bash
python manage.py makemigrations APP_NAME
```
```bash
 python manage.py migrate
 ```

 ## admin.py within APP
 ```bash
from django.contrib import admin
from .models import ChaiVarity
```

# Register your models here.
```bash
admin.site.register(ChaiVarity)
```

## now add tea within database with images

## APP/views.py
```bash
from .models import ChaiVarity
```

# Create your views here.
```bash
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})
```
## 