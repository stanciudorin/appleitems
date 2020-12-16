from django.db import models
from datetime import datetime


# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(
            upload_to='static/img', default='static/img/no-img.jpg'
                            )

    def __str__(self):
        return self.name