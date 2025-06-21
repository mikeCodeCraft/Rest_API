from rest_framework import routers
from .viewsets import HouseViewSet

app_name = 'house'

router = routers.DefaultRouter()
router.register(r'houses', HouseViewSet, basename='house')