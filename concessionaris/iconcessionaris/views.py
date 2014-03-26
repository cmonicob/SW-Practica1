from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

def mainpage(request):
	return render_to_response(
		'mainpage.html',
		{
			'titlehead': 'Sobres aPP',
			'pagetitle': 'Welcome to the Sobres aPPlication',
			'contentbody': 'Managing non legal funding since 2013',
			'user': request.user
		})
		
def clientListPage(request):
	return render_to_response('clientListPage.html',
		{
			'clients': user.all()	
		})
	"""clients = user.all()
	template =  get_template('clientListPage.html')
	output = template.render(clients)
	return HttpResponse(output)
	"""

def clientOrderPage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')

	compra = user.compra_set.all()
	template = get_template('clientOrderPage.html')
	variables = Context({
		'username': username,
		'compra': compra
	})
	output = template.render(variables)
	return HttpResponse(output)
