from rest_framework import serializers

from schedule.bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="project")
    date = serializers.DateField(read_only=True)
    start_time = serializers.TimeField(read_only=True)
    end_time = serializers.TimeField(read_only=True)
    
    class Meta:
        model = Booking
        fields = (
            'id', 
            'start', 
            'end', 
            'title', 
            'resource', 
            'resource_name', 
            'project', 
            'date',
            'start_time',
            'end_time',
        )
        ordering = ['start']

