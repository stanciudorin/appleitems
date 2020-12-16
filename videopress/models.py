from django.db import models

# Create your models here.


class Item(models.Model):
    video = models.URLField()  # same like models.URLField()
