from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse('Главная страница приложения cars')


def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')