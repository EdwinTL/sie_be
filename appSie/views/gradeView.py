from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend

from appSie.models.grade                import Grade
from appSie.serializers.gradeSerializer import GradeSerializer


class GradeCreateView(generics.CreateAPIView):
    serializer_class   = GradeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        serializer = GradeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Grado Creado", status=status.HTTP_201_CREATED)



class GradeDetailView(generics.RetrieveAPIView):
    serializer_class   = GradeSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Grade.objects.all()

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        return super().get(request, *args, **kwargs)


class GradeUpdateView(generics.UpdateAPIView):
    serializer_class   = GradeSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Grade.objects.all()

    def update(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        return super().update(request, *args, **kwargs)

class GradeDeleteView(generics.DestroyAPIView):
    serializer_class   = GradeSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Grade.objects.all()

    def deliete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        return super().destroy(request, *args, **kwargs) 

