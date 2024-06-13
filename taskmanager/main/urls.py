from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('enter/', views.enter, name='enter'),
]
