from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from .forms import *
from .models import *
from .utils import *

menu = [
    {'title': "О сайте", 'url_name': "about"},
    {'title': "Добавить статью", 'url_name': "add_page"},
    {'title': "Обратная связь", 'url_name': "contact"}
]


class CarsHome(DataMixin, ListView):
    model = Cars
    template_name = 'cars/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    # Отображает только опубликованные статьи.
    def get_queryset(self):
        return Cars.objects.filter(is_published=True).select_related('cat')


def about(request):
    return render(request, 'cars/about.html', {'menu': menu, 'login': login, 'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'cars/add_page.html'
    success_url = reverse_lazy('home')  # Перееаправление при отправке формы
    login_url = reverse_lazy('home')  # указывает адрес перенаправления для незарегистрированного пользователя

    # raise_exception = True  # Если прописать, будет появляться окно 'Доступ запрещен 403'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


def contact(request):
    return HttpResponse('Обратная связь')


class ShowPost(DataMixin, DeleteView):
    model = Cars
    template_name = 'cars/post.html'
    slug_url_kwarg = 'post_slug'  # Прописал переменную для слага использованную в urls.py
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class CarsCategory(DataMixin, ListView):
    model = Cars
    template_name = 'cars/index.html'
    context_object_name = 'posts'
    # Генерирует ошибку 404 если в категории нет статей.
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.cat_id)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    # Выбор категории по слагу.
    def get_queryset(self):
        return Cars.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'cars/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    template_name = 'cars/login.html'
    form_class = LoginUserForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
