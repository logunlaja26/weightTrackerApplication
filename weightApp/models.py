from django.db import models

class userWeight(models.Model):
    entry_date = models.DateField()
    weight_entry = models.IntegerField()

    def __str__(self):
        return str(self.entry_date)

    def __str__(self):
        return str(self.weight_entry)
