from django.db import models
from cuaderno.models import Notebook
from django.contrib.auth.models import User

# Create your models here.
#Nota
class Note(models.Model):
    title = models.CharField(max_length= 50)
    body = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(Notebook, null= True, blank= True, on_delete= models.CASCADE)

#Amistad
class Friendship(models.Model):
    friend1 = models.ForeignKey(User, null= True, blank= True, on_delete= models.CASCADE, related_name= 'friends')
    friend2 = models.ForeignKey(User, null= True, blank= True, on_delete= models.CASCADE, related_name= '_unused_friend_relation')
    class Meta:
        unique_together = ("friend1", "friend2")

class Shared(models.Model):
    owner = models.ForeignKey(User, null= True, blank= True, on_delete= models.CASCADE, related_name= 'owner')
    shared_to = models.ForeignKey(User, null= True, blank= True, on_delete= models.CASCADE, related_name= 'share_to')
    note = models.ForeignKey(Note, null= True, blank= True, on_delete= models.CASCADE, related_name= 'note')
    class Meta:
        unique_together = ("shared_to", "note")