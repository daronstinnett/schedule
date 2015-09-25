
import datetime

from django.db import models

from schedule.projects.models import Project
from schedule.resources.models import Resource


class Booking(models.Model):
    project = models.ForeignKey(Project, related_name="bookings")
    resource = models.ForeignKey(Resource, related_name="bookings")
    start = models.DateTimeField()
    end = models.DateTimeField() # TODO: add validator to ensure end day is same as start 
    
    # properties
    @property
    def resource_name(self): return self.resource.full_name
    @property
    def date(self): return self.start.date() if self.start else None
    @property
    def start_time(self): return datetime.time(self.start.hour, self.start.second) if self.start else None
    @property
    def end_time(self): return datetime.time(self.end.hour, self.end.second) if self.end else None
    
    # methods
    def __unicode__(self):
        return self.project.name + ": " + self.resource.full_name + " @ " + str(self.start)
