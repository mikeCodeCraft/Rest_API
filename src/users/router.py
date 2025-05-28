from rest_framework import routers

from .viewsets import UserViewSet, ProfileViewSet


App_Name = 'users'

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet)