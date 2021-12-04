from  django.contrib    import admin
from .models.user       import User
from .models.subject    import Subject
from .models.student    import Student
from .models.group      import Group
from .models.grade      import Grade


# Register your models here.
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Grade)