from django.urls import path

from .views import *

urlpatterns = [
    path('', CarsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('cats/<slug:cat_slug>/', CarsCategory.as_view(), name='cats'),
]
