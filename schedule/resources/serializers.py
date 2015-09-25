from rest_framework import serializers

from schedule.resources.models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resource
        fields = ('id', 'first_name', 'last_name', 'full_name')

