from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def dashboard(request):
	context = {

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
