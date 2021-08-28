from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ludotheque/', views.game_library, name='ludotheque'),
    path('search/', views.search, name='search'),
    path('details/<int:pk>/', views.details, name='details'),
]


