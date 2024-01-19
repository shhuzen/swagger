
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status,generics
from .models import ProfileModel
from .serializer import ProfileSerializer
@csrf_exempt
@api_view(['GET', 'POST'])
def Login(request):
    if request:
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:    
            token, _ = Token.objects.get_or_create(user=user)
            if _ == False:
                token.delete()
                token = Token.objects.create(user=user)
            return Response({'token': token.key},status=status.HTTP_200_OK)
        else:   
            return Response({'error': 'Ошибка Авторизации'}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.queryset.filter(user=self.request.user).first()
    def put(self, request, *args, **kwargs):
            instance,_= self.queryset.get_or_create(user=request.user)
            instance.save()
            return self.update(request, *args, **kwargs)
        

