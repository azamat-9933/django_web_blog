from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .models import *
from .forms import *


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


def add_article_view(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        form = ArticleForm()

    context = {
        "title": "Добавить статью",
        "form": form
    }

    return render(request, 'add_article.html', context)

def user_register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            # TODO: ERROR MESSAGE
            pass
    else:
        form = UserRegistrationForm()

    context = {
        "title": "Регистрация пользователя",
        "form": form
    }

    return render(request, "register.html", context)


def user_login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('index')
            else:
                # TODO: ERROR MESSAGE
                pass
        else:
            # TODO: ERROR MESSAGE
            pass
    else:
        form = UserLoginForm()
    context = {
        "title": "Войти в аккаунт",
        "form": form
    }
    return render(request, "login.html", context)


def logout_user_view(request):
    logout(request)
    return redirect('index')




