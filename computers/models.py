from django.db import models


class Computer(models.Model):
    positionID = models.IntegerField(default=0)
    name = models.CharField(max_length=128, null=True, blank=True)
    user = models.CharField(max_length=128, null=True, blank=True)
    occupied = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
