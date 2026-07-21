# Django Learning Notes

## 🐍 Python Environment Setup with uv

### Install uv

```bash
pipx install uv
```

Add `uv` to your PATH (temporary):

echo $PATH
```bash
export PATH="$HOME/.local/bin:$PATH"
```

Verify the installation:

```bash
echo $PATH
which uv
uv --version
```

---

## Create a Virtual Environment

```bash
uv venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Deactivate when finished:

```bash
deactivate
```

---

## Install Django

```bash
uv pip install Django
```

---

## Create a Django Project

```bash
django-admin startproject Project_Name(as you wish)
```

Navigate into the project:

```bash
cd Introduction
```

Run the development server:

```bash
python manage.py runserver 8001
```

---

## Make PATH Configuration Permanent

For Bash:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

For Zsh:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

# Linux Networking Commands

Check active listening ports:

```bash
ss -tuln
```

Older alternative:

```bash
netstat -tuln
```

Find which process is using a specific port:

```bash
sudo lsof -i :8080
```

---

# Django Templates

Create a `templates` directory.

Update `settings.py`:

```python
TEMPLATES = [
    {
        "DIRS": ["templates"],
    },
]
```

Render a template:

```python
return render(request, "index.html")
```

---

# Static Files

Configure static files in `settings.py`:

```python
STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

Load the static template tag:

```html
{% load static %}
```

Link a CSS file:

```html
<link rel="stylesheet" href="{% static 'style.css' %}">
```

---

## Key Concepts Learned

* Modern Python package management using **uv**
* Virtual environment creation
* Django project setup
* Running the development server
* Django template rendering
* Static file management
* Linux networking commands for debugging
* Understanding the difference between **Templates** and **Static Files**

---

## Next Topics


creating APP
python manage.py startapp

after that we should aware main project that we have a new App please know that

setting.py in Introduction folder

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "FirstAPP"
]


Tailwindcss Integration in django
https://pypi.org/project/django-tailwind/

uv pip install django-tailwind

## hot-reload
uv pip install "django-tailwind[reload]"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "FirstAPP",
    "tailwind",
    "theme",
    "django_browser_reload"
]

# if any problem occur then
python -m ensurepip --upgrade
or,
python -m pip install --upgrade pip

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "FirstAPP",
    "tailwind"
]
python manage.py tailwind init
Enter Tailwind app name [theme]:  (default will automaticatlly choosen for enter)
Choose template:
1 - Tailwind v4 Standalone - Simple and doesn't require Node.js
2 - Tailwind v4 Full - All the bells and whistles, requires Node.js
3 - Tailwind v3 Full - Legacy template for Tailwind v3 projects, requires Node.js
Enter choice [1-3]: 1

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "FirstAPP",
    "tailwind",
    "theme"
]

https://django-tailwind.readthedocs.io/en/latest/installation.html

TAILWIND_APP_NAME = "theme" (settings.py)

python manage.py tailwind install

{% load static tailwind_tags %} add this in templates layout.html
{% tailwind_css %}  add this in templates layout.html
python manage.py runserver 8002


open different terminal while server is on or off
python manage.py tailwind start

have to restart server

NPM_BIN_PATH (npm-based installation only)-but i did not install that
NPM_BIN_PATH = "/user/local/bin/npm"

https://django-tailwind.readthedocs.io/en/latest/settings.html

## TAILWIND_USE_STANDALONE_BINARY
In most cases, you don’t need to set this manually. Django Tailwind automatically detects standalone installations by checking for the presence of package.json in your theme app. If you initialized your app with --tailwind-version 4s, this detection happens automatically.

In production
python manage.py tailwind build

## auto reload
INSTALLED_APPS = [
    "django_browser_reload"
]
MIDDLEWARE = [
    "django_browser_reload.middleware.BrowserReloadMiddleware"
]

urls.py
urlpatterns = [


    path("__reload__/", include("django_browser_reload.urls"))
]

## restart both
python manage.py runserver 8002
python manage.py tailwind start