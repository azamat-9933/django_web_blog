from django.contrib.auth.models import User
from django.db import models

from django.core.validators import RegexValidator


# Create your models here.

# CREATE TABLE IF NOT EXISTS Category()

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True,
                             verbose_name="Название категории")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True,
                             verbose_name="Название статьи")
    desc = models.TextField(verbose_name="Описание статьи")
    image = models.ImageField(upload_to="articles/",
                              null=True, blank=True,
                              verbose_name="Фото статьи")
    views = models.IntegerField(default=0,
                                verbose_name="Просмотры статьи")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания статьи")
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Дата обновления статьи")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE,
                                 verbose_name="Категория статьи")
    author = models.ForeignKey(to=User, on_delete=models.CASCADE,
                               verbose_name="Автор статьи")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class TeamMember(models.Model):
    full_name = models.CharField(max_length=255,
                                 verbose_name="Имя фамилия")
    job = models.CharField(max_length=255,
                           verbose_name="Профессия")
    photo = models.ImageField(upload_to="team_members/",
                              verbose_name="Фото")
    bio = models.TextField(verbose_name="Био")
    telegram = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/t\.me\/[A-Za-z0-9_]{5,}$')
    ], verbose_name="Телеграмм")
    instagram = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/www\.instagram\.com\/[A-Za-z0-9_]{5,}$')
    ], verbose_name="Инстаграм")
    facebook = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/www\.facebook\.com\/[A-Za-z0-9_]{5,}$')
    ], verbose_name="Фейсбук")
    vkontakte = models.URLField(validators=[
        RegexValidator(r'^https?:\/\/vk\.com\/[A-Za-z0-9_]{5,}$')
    ], verbose_name="Вконтакте")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Участник команды"
        verbose_name_plural = "Участники команды"
class Profile(models.Model):
    phone = models.CharField(max_length=255,
                             null=True,
                             blank=True,
                             default="********",
                             verbose_name="Номер телефона")
    mobile = models.CharField(max_length=255,
                              null=True,
                              blank=True,
                              default="********",
                              verbose_name="Мобильный")
    address = models.CharField(max_length=255,
                               null=True,
                               blank=True,
                               default="********",
                               verbose_name="Адрес")
    job = models.CharField(max_length=255,
                           null=True,
                           blank=True,
                           default="********",
                           verbose_name="Профессия")
    image = models.ImageField(upload_to='profiles/',
                              null=True, blank=True,
                              verbose_name="Аватар")
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name="Пользователь")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name = "Автор")
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                verbose_name = "Статья")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name = "Дата добавления")
    text = models.TextField(verbose_name="Камментарий")

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"