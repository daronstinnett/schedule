from django.db import models
from django.utils.translation import ugettext as _


class Resource(models.Model):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    
    # properties
    @property
    def full_name(self): return "{first} {last}".format(first=self.first_name, last=self.last_name)
    
    # methods
    def __unicode__(self):
        return self.full_name