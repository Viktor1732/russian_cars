from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from models import *

menu = ["О сайте", "Обратная связь", "Добавить статью", "Войти"]


def index(request):
    posts = Cars.objects.all()
    return render(request, 'cars/index.html', {'menu': menu, 'title': 'Главная страница', 'posts': posts})


def about(request):
    return render(request, 'cars/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
