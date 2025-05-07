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
from users import router as users_api_router
from rest_framework_social_oauth2.urls import urlpatterns

auth_api_urls = [
    path(r'', include(('rest_framework_social_oauth2.urls', 'rest_framework_social_oauth2'), namespace='rest_framework_social_oauth2')),
]
auth_api_urls += urlpatterns

if settings.DEBUG:
    auth_api_urls.append(path(r'verify/', include('rest_framework.urls')))

api_url_patterns = [
    path(r'auth/', include(auth_api_urls)),
    path(r'accounts/', include(users_api_router.router.urls)), 
]  



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),
]


