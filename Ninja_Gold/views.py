from django.shortcuts import render, redirect
from time import localtime, strftime
import random

# Create your views here.
def index(request):
	if not 'gold' in request.session:
		request.session['gold'] = 0
	if not 'activities' in request.session:
		request.session['activities']=[]
	return render(request, 'index.html')

def process(request):
	datetime = strftime('%H:%M %p, %B %d %Y', localtime())

	if request.method == 'POST':
		if 'farm' in request.POST['location']:
			request.session['act'] = random.randrange(10,21)
			request.session['gold'] += request.session['act']
			request.session['activities'].insert(0, 'Earned {} golds from the farm'.format(request.session['act']))
		elif 'cave' in request.POST['location']:
			request.session['act'] = random.randrange(5,11)
			request.session['gold'] += request.session['act']
			request.session['activities'].insert(0, 'Earned {} golds from the cave.'.format(request.session['act']))
		elif 'house' in request.POST['location']:
			request.session['act'] = random.randrange(1,6)
			request.session['gold'] += request.session['act']
			request.session['activities'].insert(0, 'Earned {} golds from the house.'.format(request.session['act']))
		elif 'casino' in request.POST['location']:
			request.session['act'] = random.randrange(-50,31)
			request.session['gold'] += request.session['act']
			request.session['activities'].insert(0, 'Earned {} golds from the casino.'.format(request.session['act']))

	request.session.modified = True
	print(request.session['activities'])
	return redirect('/')

def reset(request):
	request.session.clear()
	return redirect('/')