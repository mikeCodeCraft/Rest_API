from django.http import HttpResponse
from django.utils.safestring import mark_safe

def api_root(request):
    return HttpResponse(mark_safe(
        '<h1>API Root</h1>'
        '<ul>'
        '<li><a href="/admin/">Admin</a></li>'
        '<li><a href="/api/auth/">api/auth/</a></li>'
        '<li><a href="/api/accounts/">api/accounts/</a></li>'
        '<li><a href="/swagger/">Swagger UI</a> </li>'
        '<li><a href="/redoc/">ReDoc</a></li>'
        '<li><a href="/">Home</a></li>'
        '</ul>'
    ))
