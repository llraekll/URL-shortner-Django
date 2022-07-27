from django.db import models

# Create your models here.


class Urls(models.Model):
    url = models.CharField(max_length=250)
    mini_url = models.CharField(max_length=20)


def __str__(self):
    return f"Here is the shorter link {self.mini_url} for {self.url}"
