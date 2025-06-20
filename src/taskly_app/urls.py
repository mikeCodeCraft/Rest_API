"""
URL configuration for taskly_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""  
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from users import router as users_api_router
from rest_framework_social_oauth2.urls import urlpatterns
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


auth_api_urls = [
    path(r'', include(('rest_framework_social_oauth2.urls', 'rest_framework_social_oauth2'), namespace='rest_framework_social_oauth2')),
]
auth_api_urls += urlpatterns

if settings.DEBUG:
    auth_api_urls.append(path(r'verify/', include('rest_framework.urls')))
    

api_url_patterns = [
    path(r'auth/', include(auth_api_urls)),
    path(r'accounts/', include(users_api_router.router.urls)), 
    path(r'accounts/', include('users.urls')),
]  

schema_view = get_schema_view(
    openapi.Info(
        title="Taskly API",
        default_version='v1',
        description="API documentation for Taskly project",
        terms_of_service="/",
        contact=openapi.Contact(email="mikecodecraft@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

