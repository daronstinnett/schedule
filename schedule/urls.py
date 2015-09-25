from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework import routers

from schedule.bookings.views import BookingViewSet
from schedule.projects.views import ProjectAPIViewSet
from schedule.resources.views import ResourceAPIViewSet


router = routers.DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'projects', ProjectAPIViewSet)
router.register(r'resources', ResourceAPIViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^bookings/', include('schedule.bookings.urls', namespace='bookings')),
    url(r'^projects/', include('schedule.projects.urls', namespace='projects')),
    
    url(r'^api/', include(router.urls, namespace="api")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]