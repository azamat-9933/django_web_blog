# Generated by Django 4.1.6 on 2024-03-05 14:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='team_members/')),
                ('bio', models.TextField()),
                ('telegram', models.URLField(validators=[django.core.validators.RegexValidator('^https?:\\/\\/t\\.me\\/[A-Za-z0-9_]{5,}$')])),
                ('instagram', models.URLField(validators=[django.core.validators.RegexValidator('^https?:\\/\\/www\\.instagram\\.com\\/[A-Za-z0-9_]{5,}$')])),
                ('facebook', models.URLField(validators=[django.core.validators.RegexValidator('^https?:\\/\\/www\\.facebook\\.com\\/[A-Za-z0-9_]{5,}$')])),
                ('vkontakte', models.URLField(validators=[django.core.validators.RegexValidator('^https?:\\/\\/vk\\.com\\/[A-Za-z0-9_]{5,}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default='********', max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, default='********', max_length=255, null=True)),
                ('address', models.CharField(blank=True, default='********', max_length=255, null=True)),
                ('job', models.CharField(blank=True, default='********', max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('desc', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles/')),
                ('views', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
    ]
