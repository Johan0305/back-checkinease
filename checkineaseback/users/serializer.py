from rest_framework import serializers
from .models import UserModel
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model= UserModel
    fields = ['id', 'name', 'lastname', 'email', 'password']
    extra_kwargs = {'password': {'write_only': True}} 
    
  def create(self, validated_data):
        # Sobrescribe el método create para cifrar la contraseña antes de crear el usuario
        user = UserModel.create_user(**validated_data)
        return user  
  
  """LOGIN"""

class UserLoginSerializer(serializers.Serializer):
    emails = serializers.EmailField()
    passwords = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        print(email, password)

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError('Correo electrónico o contraseña incorrectos')

        attrs['user'] = user
        return attrs