from django.db import models

class Indicators(models.Model):
    name = models.CharField(max_length=50)
    values = models.IntegerField(default=0)

    def __str__(self):
        return self.name