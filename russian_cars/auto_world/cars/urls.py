from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', CarsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('cats/<slug:cat_slug>/', CarsCategory.as_view(), name='cats'),
]
