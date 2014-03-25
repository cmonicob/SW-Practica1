from django.db import models
from django.contrib.auth.models import User

# Create your models here.

User.add_to_class('direccio', models.CharField(max_length=250, blank=True))
User.add_to_class('telefon', models.PositiveIntegerField(null=True, blank=True))

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
    concessionari = models.ForeignKey(Concessionari)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.user.username+" - "+self.model.name+" - "+self.concessionari.name
