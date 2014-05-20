from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404	
from iconcessionaris.models import *
from django.contrib.auth import logout
from django.core.urlresolvers import reverse	
from django.views.generic import CreateView, ListView, UpdateView, DetailView	
from forms import *	
  


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
		
class clientListPage (ListView):
    model = User
    template_name = 'clientListPage.html'

class clientDetail (DetailView):
    model = User
    template_name = 'clientInfoPage.html'

class clientOrderPage (ListView):
    model = Compra
    template_name= 'clientOrderPage.html'
    def get_queryset(self):
        return Compra.objects.filter(user=self.kwargs['pk'])


class clientCreate(CreateView):
    model = User
    template_name = 'form.html'
    form_class = ClientForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(clientCreate, self).form_valid(form)

class clientEdit(CreateView):
    model = User
    template_name = 'form.html'
    form_class = ClientForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(clientCreate, self).form_valid(form)

class carDealersListPage (ListView):
    model = Concessionari
    template_name = 'carDealersListPage.html'

class carDealersInfoPage (DetailView):
    model = Concessionari
    template_name = 'carDealersInfoPage.html'

class carDealersOrdersListPage (ListView):
    model = Compra
    template_name = 'carDealersOrderPage.html'

class cardealersCreate(CreateView):
    model = Concessionari
    template_name = 'form.html'
    form_class = CarDealerForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(cardealersCreate, self).form_valid(form)

class carDealersOrderCreate(CreateView):
    model = Compra
    template_name = 'form.html'
    form_class = CarDealerForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(carDealersOrderCreate, self).form_valid(form)

class brandsListPage(ListView):
    model = Marca
    template_name = 'brandsListPage.html'

class brandsDetail(DetailView):
    model = Marca
    template_name = 'brandsInfoPage.html'

class brandsCreate(CreateView):
    model = Marca
    template_name = 'form.html'
    form_class = BrandForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(brandsCreate, self).form_valid(form)

class ordersDetail (DetailView):
    model = Compra
    template_name = 'orderInfoPage.html'

def templateFormat(request, page):
	formatt = request.GET.get('format')
	if formatt == 'xml':
		return get_template("xml/"+page+'.xml'),"text/xml"
	if formatt == 'json':
		return get_template("json/"+page+'.json'),"application/json"
	else :
		return get_template(page+'.html'),""
