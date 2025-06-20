from django.http import HttpResponse
from django.utils.safestring import mark_safe

def api_home(request):
    return HttpResponse(mark_safe(
        '<h1>API Home</h1>'
        '<ul>'
        '<li><a href="/api/">API Root</a></li>'
        '<li><a href="/swagger/">Swagger UI</a></li>'
        '<li><a href="/redoc/">ReDoc</a></li>'
        '<li><a href="/admin/">Admin</a></li>'
        '</ul>'
    ))
