from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated


#from users.api.

class RegisterView(APIView):
    def post(self, request):
        #print("Reguistro de usuario")
        #return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#optener datos logueado
class UserView(APIView):
    permission_classes= [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    #sobreescribe para actualizar dato
    def put(self, requets):
        user = User.objects.get(id=requets.user.id)
        serializer = UserUpdateSerializer(user, requets.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)