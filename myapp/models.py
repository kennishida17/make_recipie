from django.db import models

class Dish(models.Model):
    title = models.CharField(max_length= 255)
    recipie = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
