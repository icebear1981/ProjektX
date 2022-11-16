
from django.db import models

class Kunden(models.Model):
    kdnr = models.IntegerField(primary_key=True)
    kname = models.CharField(max_length=70)
    kvname = models.CharField(max_length=70)
    kstr = models.CharField(max_length=70)
    khausnr = models.IntegerField()
    kplz = models.IntegerField()
    kort = models.CharField(max_length=70)

class Artikel(models.Model):
    artnr = models.IntegerField(primary_key=True)
    artbez = models.CharField(max_length=70)
    artpreis = models.CharField(max_length=70)

class Orders(models.Model):
    onr = models.IntegerField(primary_key=True)
    kdnr = models.ForeignKey(Kunden)
    anr = models.ForeignKey(Artikel)
    aanz = models.IntegerField()
