from django.db import models


class Operating(models.Model):
    open_hour = models.TimeField()
    close_hour = models.TimeField()
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)


# branches = models.ManyToManyField("branches.Branch", related_name="operating_hours")
