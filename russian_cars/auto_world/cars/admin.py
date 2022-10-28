from django.contrib import admin

from .models import *

#Для добавления дополнительных полей в амин-панели.
class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content') #Добавляется строка поиска по заголовку и по контенту.
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)} #Для автоматического формирования слага


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)} #Для автоматического формирования слага

#Для регистрации в админ-панели.
admin.site.register(Cars, CarsAdmin)
admin.site.register(Category, CategoryAdmin)
