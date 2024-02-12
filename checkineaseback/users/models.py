from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class UserModel (models.Model):
  name= models.CharField(max_length=255)
  lastname= models.CharField(max_length=255)
  email= models.EmailField(max_length=255, unique=True)
  password= models.TextField()

  def save(self, *args, **kwargs):
        if not self.id:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

  @classmethod       
  def create_user(cls, **kwargs):
        # Método de clase para crear un usuario con la contraseña cifrada
        password = kwargs.pop('password', None)
        if password:
            kwargs['password'] = make_password(password)
        return cls.objects.create(**kwargs)      

