from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('home/',views.home, name='home'),
    path('blog/',views.blog, name='blog'),
    path("<int:id>/",views.post, name='post'),
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact')
]

