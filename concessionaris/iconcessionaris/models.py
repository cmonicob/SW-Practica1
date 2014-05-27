from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse	
 


# Create your models here.

User.add_to_class('direccio', models.CharField(max_length=250, blank=True))
User.add_to_class('telefon', models.PositiveIntegerField(null=True, blank=True))

def get_absolute_url(self):
        return reverse('client_detail', kwargs={'pk': self.id}) 

User.add_to_class('get_absolute_url', get_absolute_url)





class Concessionari(models.Model):
    name = models.CharField(max_length=40)
    tel = models.IntegerField()
    address = models.CharField(max_length=40)
    def get_absolute_url(self):
        return reverse('carDealer_detail', kwargs={'pk': self.id})
    def __unicode__(self):
        return self.name

class Marca(models.Model):
    name = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse('brand_detail', kwargs={'pk': self.id})
    def __unicode__(self):
        return self.name

'''
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
'''

class Compra(models.Model):
    
    marca = models.ForeignKey(Marca)
    concessionari = models.ForeignKey(Concessionari)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.user.username+" - "+self.marca.name+" - "+self.concessionari.name

class Review(models.Model):
    
    concessionari = models.ForeignKey(Concessionari)
    user = models.ForeignKey(User)
    valoracio = models.IntegerField()
    comentari = models.CharField(max_length=400)
    def __unicode__(self):
        return self.user.username+" - "+self.marca.name+" - "+self.concessionari.name
