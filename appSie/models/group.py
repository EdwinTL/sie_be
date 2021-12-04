from django.db import models
from .grade     import Grade

class Group(models.Model):
    id     = models.AutoField(primary_key=True)
    name   = models.CharField(max_length = 1)
    grade  = models.ForeignKey(Grade, related_name='grade_group', on_delete=models.CASCADE)
    