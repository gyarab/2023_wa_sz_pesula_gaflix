from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=300)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    footage = models.PositiveSmallIntegerField(blank=True, null=True, help_text="pls in minutes")
    description = models.TextField(blank=True)
    main_picture = models.CharField(max_length=2048, blank=True, null=True)
    director = models.ForeignKey('Director', blank=True, null=True, on_delete=models.SET_NULL)
    actors = models.ManyToManyField('Actor', blank=True)
    genres = models.ManyToManyField('Genre', blank=True)

    def __str__(self):
        return self.name
        
    def genres_display(self):
        return ", ".join([i.name for i in self.genres.all()])

class Director(models.Model):
    name = models.CharField(max_length=300)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    main_picture = models.CharField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=300)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    main_picture = models.CharField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return self.name