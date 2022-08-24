from django.urls import path

from . import views

urlpatterns = [
    path('apply', views.apply),
    path('search_recruit_detail', views.search_recruit_detail),
    path('search', views.search),
    path('delete', views.delete),
    path('modify', views.modify),
    path('register', views.register),
]