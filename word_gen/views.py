from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


# Create your views here.
def index(request):
	if not 'count' in request.session:
		request.session['count'] = 1
	context={
		'response':get_random_string(length=10)
	}
	return render(request, 'index.html', context)

def submit(request):
	print(request.session['count'])
	request.session['count'] += 1
	print(request.POST)
	return redirect('/')

def reset(request):
	request.session['count'] = 1
	return redirect('/')
