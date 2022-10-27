from django import template

from cars.models import *

register = template.Library()  # через экземпляр Library проходит регистрация тегов


@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()

