from django.contrib import admin

# Register your models here.

from .models import Director, Movie, Genre, Language

# admin.site.register(Director)
# admin.site.register(Movie)
# admin.site.register(Genre)
# admin.site.register(Language)


class MovieInLine(admin.StackedInline):
    model = Movie
    extra = 1


class DirectorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    inlines = [MovieInLine]


# Register the Admin classes for Book using the decorator
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "director", "year", "duration")
    list_filter = ("language", "genre")


admin.site.register(Director, DirectorAdmin)
admin.site.register(Genre)
admin.site.register(Language)
