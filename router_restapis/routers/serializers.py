from rest_framework import serializers
from routers.models import Router

class RouterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Router
        fields = '__all__'