from django.db import models

# Create your models here.

class Email(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} - email by {self.name}"
