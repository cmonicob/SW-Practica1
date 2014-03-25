from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(User):
    direccio = models.CharField(max_length=250, blank=True)
    telefon = models.PositiveIntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.username

class Concessionari(models.Model):
    name = models.CharField(max_length=40)
    
    def __unicode__(self):
        return self.name

class Marca(models.Model):
    name = models.CharField(max_length=40)
    def __unicode__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=40)
    marca = models.ForeignKey(Marca)
    preu = models.IntegerField()
    def __unicode__(self):
        return self.name

class Peca(models.Model):
    name = models.CharField(max_length=40)
    model = models.ForeignKey(Model)
    def __unicode__(self):
        return self.name

class Compra(models.Model):
    model = models.ForeignKey(Model)
    concessionari = models.ForeignKey(Marca)
    client = models.ForeignKey(Client)
    def __unicode__(self):
        return self.client.username+" - "+self.model.name+" - "+self.concessionari.name
