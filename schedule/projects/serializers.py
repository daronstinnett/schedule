from rest_framework import serializers

from schedule.bookings.serializers import BookingSerializer
from schedule.projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True)
    type = serializers.StringRelatedField()
    contract = serializers.StringRelatedField()
    url = serializers.HyperlinkedIdentityField(
        view_name='projects:update'
    )
    
    class Meta:
        model = Project
        fields = (
            'id', 
            'url',
            'name', 
            'type', 
            'contract', 
            'notes',
            'bookings'
        )
    
        