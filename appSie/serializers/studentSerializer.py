from appSie.models.grade   import Grade
from appSie.models.group   import Group
from appSie.models.student import Student
from rest_framework        import serializers

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Student
        fields = ['name', 'last_name', 'gender', 'date_of_birth', 'phone', 'email', 'grade', 'group']

    
    def to_representation(self, obj):
        student     = Student.objects.get(id=obj.id)
        grade       = Grade.objects.get(id=obj.grade_id)    # clave foranea respectiva
        group       = Group.objects.get(id=obj.group_id)   
        
        return {
            'id'           : student.id,
            'name'         : student.name,
            'last_name'    : student.last_name,
            'gender'       : student.gender,
            'date_of_birth': student.date_of_birth,
            'phone'        : student.phone,
            'email'        : student.email,
            'grade' : {
                'id'           : grade.id,
                'description'  : grade.description,
            }, 
            'group' : {
                'name'           : group.name,
            }, 
        }