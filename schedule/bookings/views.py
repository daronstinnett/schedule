from django.views.generic.base import TemplateView
from rest_framework import viewsets

from schedule.bookings.filters import BookingFilter
from schedule.bookings.forms import BookingForm
from schedule.bookings.models import Booking
from schedule.bookings.serializers import BookingSerializer
from schedule.projects.forms import ProjectForm
from schedule.resources.models import Resource


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-start')
    serializer_class = BookingSerializer
    filter_class = BookingFilter
    
    
class Calendar(TemplateView):
    template_name = 'bookings/calendar.html'
    
    def get_context_data(self, **kwargs):
        data = super(Calendar, self).get_context_data(**kwargs)
        data['resources'] = Resource.objects.all().order_by('first_name')
        data['project_form'] = ProjectForm()
        data['booking_form'] = BookingForm()
        if self.request.GET.get('booking'):
            pk = int(self.request.GET.get('booking'))
            try:
                data['booking'] = Booking.objects.get(id=pk)
            except Booking.DoesNotExist:
                pass
        return data