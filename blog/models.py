from django.contrib.auth.models import User
from django.db import models

from django.core.validators import RegexValidator


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
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title


class TeamMember(models.Model):
    full_name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="team_members/")
    bio = models.TextField()
    telegram = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/t\.me\/[A-Za-z0-9_]{5,}$')
    ])
    instagram = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/www\.instagram\.com\/[A-Za-z0-9_]{5,}$')
    ])
    facebook = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/www\.facebook\.com\/[A-Za-z0-9_]{5,}$')
    ])
    vkontakte = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/vk\.com\/[A-Za-z0-9_]{5,}$')
    ])

    def __str__(self):
        return self.full_name


class Profile(models.Model):
    phone = models.CharField(max_length=255,
                             null=True,
                             blank=True,
                             default="********")
    mobile = models.CharField(max_length=255,
                              null=True,
                              blank=True,
                              default="********")
    address = models.CharField(max_length=255,
                               null=True,
                               blank=True,
                               default="********")
    job = models.CharField(max_length=255,
                           null=True,
                           blank=True,
                           default="********")
    image = models.ImageField(upload_to='profiles/',
                              null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

