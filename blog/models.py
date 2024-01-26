from django.db import models

# Create your models here.

# CREATE TABLE IF NOT EXISTS Category()

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    desc = models.TextField()
    image = models.ImageField(upload_to="articles/",
                              null=True, blank=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title