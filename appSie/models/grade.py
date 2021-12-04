from django.db import models


class Grade(models.Model):
    id          = models.CharField(primary_key=True, max_length = 15, unique=True)
    description = models.CharField(max_length=100)