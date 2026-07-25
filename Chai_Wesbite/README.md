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