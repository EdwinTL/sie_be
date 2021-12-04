from appSie.models.grade   import Grade
from appSie.models.group   import Group
from rest_framework        import serializers

class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Group
        fields = ['id','name', 'grade']

    
    def to_representation(self, obj):
        grade    = Grade.objects.get(id=obj.grade_id)    # clave foranea respectiva
        group    = Group.objects.get(id=obj.id)   # clave primaria del modelo que se esta serializando 
        return {
            'id'               : group.id,
            'grade' : {
                'id'           : grade.id,
                'description'  : grade.description,
            }
        }
