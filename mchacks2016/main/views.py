from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from main.models import *

# Create your views here.

def dashboard(request):
	user = User.objects.get(user_name='Bob')	# user_name=request.user

	context = {
		'user': user,
		'userAvailability': user.availability.all,
		'userPreferences': user.preference.all,
		'userGroups': Group.objects.filter(users__user_name='Bob')
	}
	
	return render(request, 'main/dashboard.html', context)

def group(request, group_name):
	context = {
		'group_name': group_name
	}

	return render(request, 'main/group.html', context)

def register(request):
    context = {  
    }
    
    if request.method == 'GET':
        # display empty form
        return render(request, 'main/register.html', context)
    elif request.method == 'POST': 
        # request is a POST, save user info to database
        newUser = User()
        newUser.user_name = request.POST['user_name']
        newUser.first_name = request.POST['first_name']
        newUser.last_name =request.POST['last_name']
        newUser.postal_code =request.POST['postal_code']
        newUser.password =request.POST['password']
        newUser.save()
        return render(request, 'main/dashboard.html', context)
#    else:
        #TODO: raise 404 or something
def index(request):
	context = {
	}

	return render(request, 'main/index.html', context)
