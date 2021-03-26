from django.db import models

class Tasks(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=100)
