from django import forms

from .models import *


class AddPostForm(forms.ModelForm):
    #Для того, чтобы отображалось при выборе категории "категория не выбрана".
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Cars
        fields = ['title', 'slug', 'content', 'is_published', 'cat']
        #Прописываю индивидуальные стили для полей.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
