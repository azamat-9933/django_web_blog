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


def category_page_view(request, category_id):
    articles = Article.objects.filter(category=category_id)
    trends = Article.objects.all().order_by('-views')[:5]

    context = {
        "title": f"Категория: {Category.objects.get(id=category_id).title}",
        "articles": articles,
        "trends": trends
    }

    return render(request, "category_page.html", context)


def about_us_page_view(request):
    context = {
        "title": "О нас"
    }

    return render(request, "about_us.html", context)


def our_team_page_view(request):
    context = {
        "title": "Наша команда"
    }

    return render(request, "our_team.html", context)


def services_page_view(request):
    context = {
        "title": "Наши сервисы"
    }

    return render(request, "services.html", context)


def article_detail_page_view(request, article_id):
    article = Article.objects.get(id=article_id)
    breaking_articles = Article.objects.all().order_by('-created_at')


    context = {
        "title": f"Статья: {article.title}",
        "article": article,
        "breaking_articles": breaking_articles
    }

    return render(request, "article_detail.html", context)











