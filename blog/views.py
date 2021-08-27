from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Game, all_games, all_news


def index(request):
    """View function for home page"""
    games = all_games()[:2]
    games_num = games.count()

    news = all_news()[:3]

    context = {'games': games,
               'games_num': games_num,
               'news': news,
               }
    return render(request, 'blog/index.html', context)


def game_library(request):
    """View function for ludotheque page"""
    games = all_games()
    paginator = Paginator(games, 4)  # Show 4 games per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/game_library.html', {'page_obj': page_obj})


def search(request):
    query = request.GET.get('query')
    if not query:
        games = Game.objects.all()
    else:
        games = Game.objects.filter(title__icontains=query)
    if not games.exists():
        games = Game.objects.filter(author__last_name__icontains=query)

    query_title = f"{query}"

    context = {
        'games': games,
        'query_title': query_title
    }

    return render(request, 'blog/search.html', context)
