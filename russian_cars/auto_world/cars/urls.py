from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('cats/<int:cat_id>/', show_categories, name='cats'),
]
