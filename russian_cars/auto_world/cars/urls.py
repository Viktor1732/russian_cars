from django.urls import path

from .views import *

urlpatterns = [
    path('', CarsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('cats/<slug:cat_slug>/', CarsCategory.as_view(), name='cats'),
]
