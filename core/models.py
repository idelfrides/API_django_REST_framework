from django.db import models
from attraction.models import Attraction
from adress.models import Adress
from comments.models import Comment
from evaluations.models import Evaluation


class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    aproved = models.BooleanField(default=False)
    attraction = models.ManyToManyField(Attraction)
    comment = models.ManyToManyField(Comment)
    evaluation = models.ManyToManyField(Evaluation)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE, null=True, blank=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.name


    
