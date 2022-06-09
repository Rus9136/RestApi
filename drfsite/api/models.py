from django.db import models


class news(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    sum = models.IntegerField()

    def __str__(self):
        return self.title
