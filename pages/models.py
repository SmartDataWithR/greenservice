from django.db import models
from django_pandas.managers import DataFrameManager

class List(models.Model):
    id = models.CharField(max_length = 200, primary_key=True)
    #ip_address = models.BooleanField(default = False)

    def __str__(self):
        return self.item
