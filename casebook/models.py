from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    phone=models.CharField(max_length=13)
    message=models.TextField(max_length=300)
    
    def __str__(self):
        return f"Message from {self.name}"
