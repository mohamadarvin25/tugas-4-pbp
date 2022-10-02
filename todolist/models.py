from django.db import models
from django.contrib.auth.models import User

class ItemTodolist(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.TextField()
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default=False)