from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	if not 'count' in request.session:
		request.session['count'] = 0;
	
	return render(request, 'index.html')

def submit(request):
	request.session['count'] += 1;
	request.session['name'] = request.POST['name']
	request.session['campus'] = request.POST['campus']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	print(request.POST)
	return redirect('/created')

def created(request):
	return render(request, 'created.html')

def goback(request):
	return redirect('/')