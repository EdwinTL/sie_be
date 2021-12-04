from django.db  import models
from .grade     import Grade
from .group     import Group



class Student(models.Model):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length = 15, unique=True)
    last_name       = models.CharField(max_length = 30)
    gender          = models.CharField(max_length = 30)
    date_of_birth   = models.DateField(blank=True)
    phone           = models.CharField(max_length =15)
    email           = models.EmailField(max_length = 100)
    grade           = models.ForeignKey(Grade, related_name='grade_student', on_delete=models.CASCADE)
    group           = models.ForeignKey(Group, related_name='group_student', on_delete=models.CASCADE)