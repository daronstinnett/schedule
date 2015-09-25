from rest_framework import viewsets

from schedule.resources.models import Resource
from schedule.resources.serializers import ResourceSerializer


class ResourceAPIViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all().order_by('first_name')
    serializer_class = ResourceSerializer
    