from django.db import models
from cuaderno.models import Cuaderno
from django.contrib.auth.models import User

# Create your models here.
#Nota
class Nota(models.Model):
    titulo= models.CharField(max_length= 50)
    contenido= models.TextField(null=True, blank=True)
    pertenece= models.ForeignKey(Cuaderno, null= True, blank= True, on_delete= models.CASCADE)

#Amistad
class Amistad(models.Model):
    amigo1= models.ForeignKey(User, null= True, blank= True, on_delete= models.CASCADE, related_name= 'friends')
    amigo2= models.ForeignKey(User, null= True, blank= True, on_delete= models.CASCADE, related_name= '_unused_friend_relation')

class Compartido(models.Model):
    dueno= models.ForeignKey(User, null= True, blank= True, on_delete= models.CASCADE, related_name= 'owner')
    compartido= models.ForeignKey(User, null= True, blank= True, on_delete= models.CASCADE, related_name= 'share_to')
    nota= models.ForeignKey(Nota, null= True, blank= True, on_delete= models.CASCADE, related_name= 'note')