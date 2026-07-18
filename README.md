# Django Learning Notes

## 🐍 Python Environment Setup with uv

### Install uv

```bash
pipx install uv
```

Add `uv` to your PATH (temporary):

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
django-admin startproject Introduction
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


