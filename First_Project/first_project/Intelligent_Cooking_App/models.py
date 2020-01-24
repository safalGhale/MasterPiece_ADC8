from django.db import models

class Recipes(models.Model):
    Username = models.CharField(max_length=50)
    Dishname = models.CharField(max_length=50)
    Recipe = models.TextField()

    def __str__(self):
        return self.Username + " " + self.Dishname + " " + self.Recipe
    