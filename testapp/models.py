from django.db import models

# Create your models here.


class Cube(models.Model):
    value = models.IntegerField(default=0)

    def __str__(self):
        return f'cub {self.pk}'
