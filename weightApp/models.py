from django.db import models

class userWeight(models.Model):
    entry_date = models.DateField()
    weight_entry = models.IntegerField()
