from django.db import models

# Create your models here.

class StarterDeck (models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class Card (models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    deck = models.ForeignKey(to=StarterDeck, on_delete=models.CASCADE)

    def __str__(self):
        return self.title