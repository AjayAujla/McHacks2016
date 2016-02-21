from django.http import HttpResponse
from django.shortcuts import render
from main.models import *

# Create your views here.

def dashboard(request):
	availabilities = Availability.objects.filter(user__user_name='Bob')	# user__user_name=request.user

	context = {
		'my_availabilities': availabilities
	}
	
	return render(request, 'main/dashboard.html', context)

def group(request, group_name):
	context = {
		'group_name': group_name
	}

	return render(request, 'main/group.html', context)

def index(request):
	context = {
	}

	return render(request, 'main/index.html', context)
