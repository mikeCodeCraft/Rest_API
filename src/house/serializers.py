from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['url', 'id', 'name', 'image', 'created_on', 'description', 'manager','members_count', 'points', 'completeted_tasks_count', "notcompleted_tasks_count" ]
        
        
        read_only_fields = ('id', 'created_on', 'manager', 'points', 'completed_tasks_count', 'notcompleted_tasks_count')
    
    # def create(self, validated_data):
    #     # Automatically set the manager to the current user
    #     request = self.context.get('request')
    #     if request and hasattr(request, 'user'):
    #         validated_data['manager'] = request.user.profile
    #     return super().create(validated_data)