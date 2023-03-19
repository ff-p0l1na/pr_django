from django.db import models


class Fiszka(models.Model):
    przod = models.CharField('Przód karty', max_length=100)
    tyl = models.CharField('Tył karty', max_length=100)
    mnemo = models.CharField('Zdanie ułatwiające zapamiętanie', max_length=300)

    def __str__(self):
        return self.przod

# class Rezultat(models.Model):


