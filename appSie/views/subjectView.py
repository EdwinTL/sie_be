from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend


from appSie.models.subject                  import Subject
from appSie.serializers.subjectSerializer   import SubjectSerializer



class SubjectCreateView(generics.CreateAPIView):
    serializer_class   = SubjectSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        serializer = SubjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Asignatura Creada Exitosamente", status=status.HTTP_201_CREATED)


class SubjectDeleteView(generics.DestroyAPIView):
    serializer_class   = SubjectSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Subject.objects.all()

    def deliete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        return super().destroy(request, *args, **kwargs)
