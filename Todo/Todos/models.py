from django.db import models
from django.utils import timezone
class Tasks(models.Model):
    added_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=100)
