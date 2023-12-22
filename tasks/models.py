from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    descriptio = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#esta funcion se define para que en el titulo de las tareas te muestre el titulo de la tarea y no object1, object2 etc y de paso se concatenó con el usuario que lo creó
    def __str__(self):
        return self.title + ' hecho por: ' + self.user.username
