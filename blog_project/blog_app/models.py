from django.db import models

# Create your models here.

class Blog_All(models.Model):
    blog_header = models.CharField(max_length=150)
    blog_author = models.CharField(max_length=15)
    blog_creatat = models.DateTimeField(auto_now_add=True)
    blog_image = models.ImageField(upload_to= 'upload/', blank=True, null=True)
    blog_content = models.TextField(max_length=3000)

    def __str__(self):
        return f"Your {self.blog_header} has been stored."


class About_Me(models.Model):
    intro_header = models.CharField(max_length=150)
    intro_createdat = models.DateTimeField(auto_now_add=True)
    intro_image = models.ImageField(upload_to= 'upload/', blank=True, null=True)
    intro_content = models.TextField(max_length=3000)

    def __str__(self):
        return f"Your {self.intro_header} has been stored."


