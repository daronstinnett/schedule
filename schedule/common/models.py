from django.db import models

class ListItem(models.Model):
    name = models.CharField(max_length=31)
    
    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name
