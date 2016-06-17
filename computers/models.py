from django.db import models


class Computer(models.Model):
    name = models.CharField(max_length=128)
    occupied = models.BooleanField(default=False)
    user = models.CharField(max_length=128, null=True, blank=True)
    positionID = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name
