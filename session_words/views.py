from django.shortcuts import render, redirect
from time import localtime, strftime
# Create your views here.
def index(request):
	print(request.session.get('color'))
	print(request.session.get('size'))
	print(request.session.get('word'))
	return render(request, 'index.html')

def submit(request):
	if not 'word' in request.session:
		request.session['word']=[]

	if request.method == 'POST':
		datetime = strftime('%H:%M %p, %B %d %Y', localtime())
		if 'word' in request.POST:
			values ={
			'word': request.POST['word'],
			'color': request.POST['color'],
			'size': request.POST['size'],
			'datetime': datetime
			}
	request.session['word'].append(values)
	request.session.modified = True
	print(request.POST)
	print(request.session.__dict__)
	return redirect('/')

def reset(request):
	request.session.clear()
	return redirect('/')