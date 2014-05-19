from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404	
from iconcessionaris.models import *
from django.contrib.auth import logout
from django.core.urlresolvers import reverse	
from django.views.generic import DetailView	
from django.views.generic.edit import CreateView	
  

from	
  forms	
  import	
  RestaurantForm,	
  DishForm	
  


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def mainpage(request):
	return render_to_response(
		'mainpage.html',
		{
			'titlehead': 'Concessionaris APP',
			'pagetitle': 'Benvingut a l\'aplicacio per gestionar els concessionaris',
			'user': request.user
		})
		
def clientListPage(request):
	try:
		clients = User.objects.all()
		
	except:
		raise Http404('User List not found')
	template, mimetype = templateFormat(request,'clientListPage')
	variables = Context({
		'clients' : clients
	})
	output = template.render(variables)
	return HttpResponse(output, mimetype=mimetype)

def clientInfoPage(request, username):
	try:
		client = User.objects.get(username=username)
	except:
		raise Http404('User not found.')
	template, mimetype = templateFormat(request,'clientInfoPage')
	variables = Context({
		'client' : client
	})
	output = template.render(variables)
	return HttpResponse(output, mimetype=mimetype)

def clientOrderPage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')

	orders = user.compra_set.all()
	template, mimetype = templateFormat(request,'clientOrderPage')
	variables = Context({
		'username': username,
		'orders': orders
	})
	output = template.render(variables)
	return HttpResponse(output, mimetype=mimetype)

class clientCreate(CreateView):
    model = User
    template_name = 'iconcessionaris/templates/form.html'
    form_class = ClientForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(clientCreate, self).form_valid(form)

def carDealersListPage(request):
	try:
		carDealers = Concessionari.objects.all()
	except:
		raise Http404('CarDealers List not found')
	template, mimetype = templateFormat(request,'carDealersListPage')
	variables = Context({
		'carDealers' : carDealers
	})
	output = template.render(variables)
	return HttpResponse(output, mimetype=mimetype)

def carDealersInfoPage(request, name) :
	try:
		concessionari = Concessionari.objects.get(name=name)
	except:
		raise Http404('User not found.')
	template, mimetype = templateFormat(request,'carDealersInfoPage')
	variables = Context({
		'concessionari' : concessionari
	})
	output = template.render(variables)
	return HttpResponse(output, mimetype=mimetype)

def carDealersOrderPage(request, name):
	try:
		carDealers = Concessionari.objects.get(name=name)
	except:
		raise Http404('carDealer not found.')

	orders = carDealers.compra_set.all()
	template, mimetype = templateFormat(request,'carDealersOrderPage')
	variables = Context({
		'carDealer': name,
		'orders': orders
	})
	output = template.render(variables)
	return HttpResponse(output, mimetype=mimetype)


def brandsListPage(request):

	try:
		brands = Marca.objects.all()
	except:
		raise Http404('Brands List not found')
	template, mimetype = templateFormat(request,'brandsListPage')
	variables = Context({
		'brands' : brands
	})
	output = template.render(variables)
	return HttpResponse(output, mimetype=mimetype)

def brandsInfoPage (request, name):
	try:
		brand = Marca.objects.get(name=name)
	except:
		raise Http404('Brand not found.')
	template, mimetype = templateFormat(request,'brandsInfoPage')
	variables = Context({
		'brand' : brand
	})
	output = template.render(variables)
	return HttpResponse(output, mimetype=mimetype)

def ordersInfoPage(request, orderid):
	try:
		order = Compra.objects.get(id=orderid)
	except:
		raise Http404('Order not found.')
	template, mimetype = templateFormat(request,'orderInfoPage')
	variables = Context({
		'order' : order
	})
	output = template.render(variables)
	return HttpResponse(output, mimetype=mimetype)

def templateFormat(request, page):
	formatt = request.GET.get('format')
	if formatt == 'xml':
		return get_template("xml/"+page+'.xml'),"text/xml"
	if formatt == 'json':
		return get_template("json/"+page+'.json'),"application/json"
	else :
		return get_template(page+'.html'),""
