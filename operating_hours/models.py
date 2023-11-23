from django.db import models
import uuid


class Operating(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    open_hour = models.TimeField()
    close_hour = models.TimeField()
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
