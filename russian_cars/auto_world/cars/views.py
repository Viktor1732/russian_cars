from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from .models import *

menu = [
    {'title': "О сайте", 'url_name': "about"},
    {'title': "Добавить статью", 'url_name': "add_page"},
    {'title': "Обратная связь", 'url_name': "contact"}
]
login = ["Регистрация", "Войти"]


def index(request):
    posts = Cars.objects.all()
    cats = Category.objects.all()

    context = {
        'cats': cats,
        'cat_selected': 0,
        'login': login,
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts
    }
    return render(request, 'cars/index.html', context=context)


def about(request):
    return render(request, 'cars/about.html', {'menu': menu, 'login': login, 'title': 'О сайте'})


def add_page(request):
    return HttpResponse('Добавить статью')


def contact(request):
    return HttpResponse('Обратная связь')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с номером id: {post_id}')


def show_categories(request, cat_id):
    posts = Cars.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'cats': cats,
        'cat_selected': cat_id,
        'login': login,
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts
    }
    return render(request, 'cars/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
