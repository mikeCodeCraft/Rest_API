from rest_framework import routers

from .viewsets import UserViewSet


App_Name = 'users'

router = routers.DefaultRouter()
router.register('users', UserViewSet)