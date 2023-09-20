from django.db import models

# Create your models here.

class Review(models.Model):
    user_name=models.CharField(max_length=50)
    review_text=models.TextField(max_length=200)
    ratings=models.IntegerField()

    def __str__(self):
        return f"{self.user_name}'s review"
    
