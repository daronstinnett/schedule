from django.db import models
from django.utils.translation import ugettext as _

from schedule.common.models import ListItem


class Contract(ListItem):
    pass

class Type(ListItem):
    pass

class Project(models.Model):
    name = models.CharField(_('name'), max_length=63)
    type = models.ForeignKey(Type)
    contract = models.ForeignKey(Contract)
    notes = models.TextField(blank=True, null=True)
    
    # methods
    def __unicode__(self):
        return self.name
