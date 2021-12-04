from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend


from appSie.models.student                  import Student
from appSie.serializers.studentSerializer   import StudentSerializer


class StudentCreateView(generics.CreateAPIView):
    serializer_class   = StudentSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Estudiante Creado Exitosamente", status=status.HTTP_201_CREATED)


class StudentDetailView(generics.RetrieveAPIView):
    serializer_class   = StudentSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Student.objects.all()

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        
        return super().get(request, *args, **kwargs)


class StudentDeleteView(generics.DestroyAPIView):
    serializer_class   = StudentSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Student.objects.all()

    def deliete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        return super().destroy(request, *args, **kwargs)
