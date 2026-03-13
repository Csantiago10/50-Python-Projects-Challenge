from django.db import models

# Create your models here.
class Article(models.Model):
    # Defined fields for the model
    title  = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    # String representation of the model
    def __str__(self):
        return f"{self.title} by {self.author}"