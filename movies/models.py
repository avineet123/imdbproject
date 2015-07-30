from django.db import models

# Create your models here


class GenreModel(models.Model):
    genre_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.genre_name)


class MovieModel(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    popularity_99 = models.DecimalField(max_digits=4, decimal_places=1)
    imdb_score = models.DecimalField(max_digits=4, decimal_places=1)
    genre = models.ManyToManyField(GenreModel)
