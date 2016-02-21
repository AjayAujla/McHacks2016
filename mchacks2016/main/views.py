from django.http import HttpResponse
from django.shortcuts import render
from main.models import *

# Create your views here.

def dashboard(request):
	user = User.objects.get(user_name='Bob')	# user_name=request.user

	context = {
		'user': user,
		'userAvailability': user.availability.all
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
