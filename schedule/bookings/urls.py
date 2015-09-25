from django.conf.urls import url

from schedule.bookings.views import Calendar


urlpatterns = [
    url(r'^calendar/$', Calendar.as_view(), name="calendar"),
]  
