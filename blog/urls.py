from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ludotheque/', views.game_library, name='ludotheque'),
    path('search/', views.search, name='search'),
    path('details-game/<int:pk>/', views.details_game, name='details-game'),
    path('details-news/<int:pk>/', views.details_news, name='details-news'),
    path('news/', views.news_page, name='news'),
]


