from appSie.models.grade    import Grade
from rest_framework         import serializers

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Grade
        fields = ['id', 'description']

    def to_representation(self, obj):
        grade = Grade.objects.get(id=obj.id)   # clave primaria del modelo que se esta serializando 
        return {
            'id'               : grade.id,
            'description'      : grade.description,

        }