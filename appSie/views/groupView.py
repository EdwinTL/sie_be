from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend


from appSie.models.group                import Group
from appSie.serializers.groupSerializer import GroupSerializer


class GroupCreateView(generics.CreateAPIView):
    serializer_class   = GroupSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        serializer = GroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Grupo Creado", status=status.HTTP_201_CREATED)

class GroupDetailView(generics.RetrieveAPIView):
    serializer_class   = GroupSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Group.objects.all()

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        
        return super().get(request, *args, **kwargs)

class GroupDeleteView(generics.DestroyAPIView):
    serializer_class   = GroupSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Group.objects.all()

    def deliete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        return super().destroy(request, *args, **kwargs)

