from django.contrib import admin

from .models import Author, Game, Editor, News

admin.site.register(Editor)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_author', 'display_editor']
    list_filter = ('author', 'editor', 'year')


@admin.register(News)
class News(admin.ModelAdmin):
    list_display = ['title', 'date_created']

