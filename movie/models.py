from django.db import models
from common.models import Lang
from person.models import Person, Job


class Country(models.Model):
    """
    `Country` represents a country where the movie or user is.

    Attributes:
        lang: foreign key with Lang table identify the language.
        code: The code is a string like 'es' or 'en'.
        name: Name for the country like 'Spain'
    """
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


class Genre(models.Model):
    """
    `Genre` represents the types of differents movie genres. Example 'Action, 
    Adventure'

    Attributes:
        id_tmdb: reference to tmdb genre.
        langs: many to many fields with Lang table.
    """
    id_tmdb = models.IntegerField(null=True, blank=True)
    langs = models.ManyToManyField(Lang, through='Genre_lang')


class Genre_lang(models.Model):
    """
    `Genre Lang` represents genre in diferents languages.

    Attributes:
        genre: Foreign Key that link to Genre.
        lang: link to lang table.
        name: The name of genre.
    """
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Source(models.Model):
    """
    `Source` have a amount of diferents ratings pages. Example: IMDB, Tviso ...

    Attributes:
        name: name of the site. Example: IMDB
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie (models.Model):
    """
    `Movie` is a audiovisual resource with diferents links to people like 
    actors, people ..

    Attributes:
    """
    original_title = models.CharField(max_length=100)
    backdrop = models.URLField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    average = models.DecimalField(decimal_places=3, max_digits=5, null=True, 
                                  blank=True)
    cast = models.ManyToManyField(Person, through='Cast', blank=True)
    langs = models.ManyToManyField(Lang, through='Movie_lang', blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    ratings = models.ManyToManyField(Source, through='Rating', blank=True)

    def __str__(self):
        return self.original_title


class Movie_lang(models.Model):
    """
    `Movie_lang` is a translation for Movie

    Attributes:
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, null=True, blank=True, 
                                on_delete=models.SET_NULL)
    title = models.CharField(max_length=300)
    overview = models.TextField(null=True, blank=True)
    poster = models.URLField(null=True, blank=True)
    trailer = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title


class Cast(models.Model):
    """
    `Cast` is a intermediate table between Movie to Person and Job that 
    represents the diferent people involve in a movie and his diferents roles.
    Attributes:
    """
    movie = models.ForeignKey(Movie, related_name="movie_cast", 
                              on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (('movie', 'person', 'job'),)


class Company(models.Model):
    """
    `Company` represents the diferents companies in the world cinema.

    Attributes:
    """
    name = models.CharField(max_length=100)
    logo = models.URLField(null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    """
    `Rating` is measure that can be aplied to a 'Movie'.

    Attributes:
    """
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    sourceid = models.CharField(max_length=200, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=0)
    count = models.IntegerField(null=True, blank=True)
    date_update = models.DateField(auto_now=True)
