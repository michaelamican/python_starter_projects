from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Course, Description

# Create your views here.
def index(request):
	course = Course.objects.all()
	description = Description.objects.all()
	context = {
		'course':course,
		'description':description
	}
	return render(request, 'index.html', context)

def warning(request, course_id):
	course_id = Course.objects.get(id = course_id)
	context = {
		'course':course
	}
	return render(request, 'warning.html', context)

def add(request):
	if request.method == 'POST':
		f = request.POST
		g = request.POST
		has_errors = False
		if len(f['course']) < 1:
			has_errors = True
			messages.error(request, 'Please enter a name')
		if len(f['description'])<10:
			has_errors=True
			messages.error(request, 'Please enter a description')
		if has_errors == True:
			return redirect('/')
		else:
			course = Course.objects.create(course=f['course']) 
			description = Description.objects.create(description = f['description'], courses_description = course_id)
	return redirect('/')

def delete(request, course_id):
	if request.method == 'GET':
		course = Course.objects.filter(id = course_id)

		return redirect('/warning')

def begone(request):
	if request.method == 'POST':
		course = Course.objects.filter(id = course_id)
		
		return redirect(request, 'index.html')