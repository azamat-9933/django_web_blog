from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    readonly_fields = ('views', 'author')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user

        super(ArticleAdmin, self).save_model(
            request, obj, form, change
        )


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile)
admin.site.register(TeamMember)

