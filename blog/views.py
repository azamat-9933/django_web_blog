from django.shortcuts import render

from .models import *


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()


    context = {
        "title": "Главная страница",
        "categories": categories,
        "articles": articles
    }


    return render(request, "main_page.html", context)
