import os
import uuid
from django.db import models
from django.utils.deconstruct import deconstructible

@deconstructible
class GenerateHouseImagePath(object):
    
    def __init__(self):
        pass
    
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f"media/houses/{instance.id}/images"
        name = f'main.{ext}'
        return os.path.join(path, name)

house_image_path = GenerateHouseImagePath()
class House(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='house_image_path', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    manager = models.OneToOneField('users.Profile', on_delete=models.SET_NULL, related_name='manage_house', blank=True, null=True)
    points = models.IntegerField(default=0)
    completed_tasks_count = models.IntegerField(default=0)
    notcompleted_tasks_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name