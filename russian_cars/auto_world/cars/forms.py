from django import forms

from .models import *


class AddPostForm(forms.Form):
    """Так прописываем класс widget=forms.TextInput(attrs={'......': '........'}, который используем в CSS"""
    title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Контент")
    # required=False - Делает поле необязательным для заполнения, initial=True - делает чекбокс отмеченным.
    is_published = forms.BooleanField(label="Публикация", initial=True, required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label='Категория не выбрана')
