from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView

from .forms import *
from .models import *

menu = [
    {'title': "О сайте", 'url_name': "about"},
    {'title': "Добавить статью", 'url_name': "add_page"},
    {'title': "Обратная связь", 'url_name': "contact"}
]
login = ["Регистрация", "Войти"]


class CarsHome(ListView):
    model = Cars
    template_name = 'cars/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    # Отображает только опубликованные статьи.
    def get_queryset(self):
        return Cars.objects.filter(is_published=True)


def about(request):
    return render(request, 'cars/about.html', {'menu': menu, 'login': login, 'title': 'О сайте'})


def add_page(request):
    """#Проверка формы на заполнение. Если на момент отправки форма заполнена не корректно,
    то вернется заполненная форма."""
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)  # request.FILES - список файлов, переданных на сервер из формы.
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'cars/add_page.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('Обратная связь')


class ShowPost(DeleteView):
    model = Cars
    template_name = 'cars/post.html'
    slug_url_kwarg = 'post_slug'  # Прописал переменную для слага использованную в urls.py
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context



class CarsCategory(ListView):
    model = Cars
    template_name = 'cars/index.html'
    context_object_name = 'posts'
    # Генерирует ошибку 404 если в категории нет статей.
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    # Выбор категории по слагу.
    def get_queryset(self):
        return Cars.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
