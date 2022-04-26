from django.db import models
from django.urls import reverse

# Create your models here.


# Genre
class Genre(models.Model):
    name = models.CharField(
        max_length=200, help_text="Enter a movie genre (e.g. Fiction, Horror, etc.)"
    )

    def __str__(self):
        return self.name


# Language
class Language(models.Model):
    language = models.CharField(
        max_length=200,
        help_text="Enter movie language (e.g. English, Spanish, French, etc.)",
    )

    def __str__(self):
        return self.language


# Directors
class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()
    picture = models.URLField()
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)


# Movies
class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey("Director", on_delete=models.CASCADE, null=True)
    plot = models.TextField()
    imdb = models.URLField(help_text="IMDB url")
    genre = models.ManyToManyField(Genre)
    language = models.ManyToManyField(Language)
    poster = models.URLField()
    year = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Movie duration in minutes")

    def duration_hours(self):

        hours = self.duration // 60
        minutes = self.duration % 60
        # Create time as a string
        time = "{}h {}m".format(hours, minutes)
        return time

    def __str__(self):
        return self.title
