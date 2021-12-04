from appSie.models.grade     import Grade
from appSie.models.subject   import Subject
from rest_framework          import serializers

class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Subject
        fields = ['id', 'name', 'grade']

    
    def to_representation(self, obj):
        grade      = Grade.objects.get(id=obj.grade_id)    # clave foranea respectiva
        subject    = Subject.objects.get(id=obj.id)   # clave primaria del modelo que se esta serializando 
        return {
            'id'               : subject.id,
            'name'             : subject.name,
            'grade' : {
                'id'           : grade.id,
                'description'  : grade.description,
            }
        }