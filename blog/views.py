from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()[:5]

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
    comments = Comment.objects.filter(article=article_id)
    if request.user.id != article.author.id:
        article.views += 1
        article.save()

    context = {
        "title": f"Статья: {article.title}",
        "article": article,
        "breaking_articles": breaking_articles,
        "comments": comments
    }

    if request.user.is_authenticated:
        context.update({
            "form": CommentForm()
        })

    return render(request, "article_detail.html", context)

@login_required(login_url="login")
def add_article_view(request):
    if request.method == "POST":
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Статья успешно добавлена !")
            return redirect("article_detail", article.id)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect("add_article")
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
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(request, "Вы успешно прошли регистрацию !")
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('register')
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
                messages.success(request, "Вы вошли в аккаунт !")
                return redirect('index')
            else:
                messages.error(request, "Логин или пароль неправильный !")
                return redirect('login')
        else:
            messages.error(request, "Логин или пароль неправильный !")
            return redirect('login')
    else:
        form = UserLoginForm()
    context = {
        "title": "Войти в аккаунт",
        "form": form
    }
    return render(request, "login.html", context)

@login_required(login_url="login")
def logout_user_view(request):
    logout(request)
    messages.info(request, "Вы вышли с аккаунта !")
    return redirect('index')

@login_required(login_url="login")
def update_article_view(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == 'POST':
        form = ArticleForm(instance=article,
                           data=request.POST,
                           files=request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Статья успешно обновлена !")
            return redirect("article_detail", article.id)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect("update_article", article.id)
    else:
        form = ArticleForm(instance=article)

    context = {
        "form": form,
        "title": "Изменить статью"
    }
    return render(request, "add_article.html", context)

@login_required(login_url="login")
def delete_article_view(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == "POST":
        article.delete()
        messages.warning(request, "Статья удалена !")
        return redirect("index")

    context = {
        "title": "Удаление статьи",
        "article": article
    }

    return render(request, "delete.html", context)


def search_view(request):
    word = request.GET.get("q")
    categories = Category.objects.all()
    articles = Article.objects.filter(
        title__iregex=word
    )

    context = {
        "articles": articles,
        "categories": categories,
        "title": "Результаты поиска"
    }
    messages.info(request, "Результаты поиска !")
    return render(request, "main_page.html", context)

@login_required(login_url="login")
def profile_page_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    context = {
        "profile": profile,
        "title": "Мой профиль"
    }

    return render(request, "profile.html", context)

@login_required(login_url="login")
def edit_profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        user_form = UserForm(instance=user, data=request.POST)
        profile_form = ProfileForm(instance=profile, data=request.POST,
                                   files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Данные профиля успешно обновлены !")
            return redirect("profile", user.id)
        else:
            for field in user_form.errors:
                messages.error(request, user_form.errors[field].as_text())
            for field in profile_form.errors:
                messages.error(request, profile_form.errors[field].as_text())
            return redirect("edit_profile", user.id)
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "title": "Изменить профиль"
    }
    return render(request, "edit_profile.html", context)

@login_required(login_url="login")
def save_comment(request, article_id):
    article = Article.objects.get(id=article_id)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.author = request.user
        comment.save()
        messages.success(request, "Комментарии успешно добавлено !")
        return redirect('article_detail', article_id)
