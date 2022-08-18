from django.urls import path

from . import views

urlpatterns = [
    path('search_recruit_detail/', views.search_recruit_detail),
    path('search/', views.search),
    path('search/<str:keyword>', views.search),
    path('delete/', views.delete),
    path('modify/', views.modify),
    path('register/', views.register),
    path('', views.index, name='index'),
]