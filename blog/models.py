from django.db import models
from cloudinary.models import CloudinaryField


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']  # classement dans la BD

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Editor(models.Model):
    name = models.CharField(max_length=100)
    web_site = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Game(models.Model):
    LANGUAGES = [('fr', 'Francais'),
                 ('en', 'Anglais')]
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=2048, blank=True)
    author = models.ManyToManyField(Author)
    editor = models.ManyToManyField(Editor)
    language = models.CharField(max_length=150, choices=LANGUAGES, blank=True)
    year = models.CharField(max_length=4)
    image = CloudinaryField('image')
    date_created = models.DateTimeField(auto_now=True)
    has_extension = models.BooleanField(default=False)
    is_extension = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def display_author(self):
        """Crée une chaine de caractères pour les auteurs. Nécessaire pour afficher auteur dans admin"""
        return ', '.join(author.__str__() for author in self.author.all()[:3])

    def display_editor(self):
        """Crée une chaine de caractères pour les editeurs. Nécessaire pour afficher editeur dans admin"""
        return ', '.join(editor.__str__() for editor in self.editor.all()[:3])


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2048, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


def all_games():
    """creates a list of all games"""
    return Game.objects.all()


def all_news():
    """Creates a list of all news"""
    return News.objects.all()
