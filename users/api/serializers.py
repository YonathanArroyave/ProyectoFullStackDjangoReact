from rest_framework import serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id', 'email', 'username', 'password' ]
    #sobreescritura del metodo crear usuarios para las contraseñass queden encriptadas
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password) 
        instance.save()
        return instance
#serializar para consulta
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'email', 'username', 'first_name', 'last_name']
#serializador para actualizar usuario logeado
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['first_name', 'last_name']#pip install djangorestframework-simplejwt