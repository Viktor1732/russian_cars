from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *

menu = [
    {'title': "О сайте", 'url_name': "about"},
    {'title': "Добавить статью", 'url_name': "add_page"},
    {'title': "Обратная связь", 'url_name': "contact"}
]
login = ["Регистрация", "Войти"]


def index(request):
    posts = Cars.objects.all()

    context = {
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
    """#Проверка формы на заполнение. Если на момент отправки форма заполнена не корректно,
    то вернется заполненная форма."""
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Cars.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    return render(request, 'cars/add_page.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('Обратная связь')


def show_post(request, post_slug):
    post = get_object_or_404(Cars, slug=post_slug)

    context = {
        'cat_selected': post.cat_id,
        'login': login,
        'menu': menu,
        'title': post.title,
        'post': post
    }
    return render(request, 'cars/post.html', context=context)


def show_categories(request, cat_id):
    posts = Cars.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'cat_selected': cat_id,
        'login': login,
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts
    }
    return render(request, 'cars/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
