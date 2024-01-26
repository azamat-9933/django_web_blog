from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    readonly_fields = ('views',)


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
