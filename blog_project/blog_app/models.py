from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    post_on = models.DateTimeField(max_length=20)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    content = models.TextField(max_length=5000)

    def __str__(self):
        return f"{self.title} by {self.author}"

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username} created."