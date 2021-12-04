from django.db import models
from .grade     import Grade

class Subject(models.Model):
    id     = models.AutoField(primary_key=True)
    name   = models.CharField(max_length = 15)
    grade  = models.ForeignKey(Grade, related_name='subject_grade', on_delete=models.CASCADE)
    