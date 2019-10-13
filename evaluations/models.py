from django.db import models
from django.contrib.auth.models import User


class Evaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    value = models.DecimalField(max_digits=2, decimal_places=1)
    date = models.DateTimeField(auto_now_add=True)
    # auto_now_add: adiciona data e hora 
    # automaticamente quano o campo é adicionado


    def __str__(self):
        return self.user.username