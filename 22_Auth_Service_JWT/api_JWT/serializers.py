from rest_framework import serializers
from .models import Computer

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ['id', 'brand', 'motherboard', 'processor', 'ram', 'storage', 'monitor', 'keyboard', 'mouse']