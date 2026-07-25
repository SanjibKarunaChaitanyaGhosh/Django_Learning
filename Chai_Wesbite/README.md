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

