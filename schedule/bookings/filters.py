import rest_framework_filters as filters
from schedule.bookings.models import Booking


class BookingFilter(filters.FilterSet):

    class Meta:
        model = Booking
        fields = ['resource__id']