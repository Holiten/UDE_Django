from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    wikipedia = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Book(models.Model):
    AVENTURE = "AV"
    THRILLER = "TR"
    FANTASY = "FS"
    ROMANCE = "RM"
    HORROR = "HR"
    SCIENCE_FICTION = "SF"
    GENRE = [
        (AVENTURE, 'Aventure'),
        (THRILLER, 'Thriller'),
        (FANTASY, 'Fantasy'),
        (ROMANCE, 'Romance'),
        (HORROR, 'Horreur'),
        (SCIENCE_FICTION, 'Sciences-Fiction')
    ]
    title = models.CharField(max_length=100)
    price = models.FloatField(blank=True)
    summary = models.TextField(blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True)
    category = models.CharField(max_length=50, choices=GENRE, blank=True)
    stock = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title
