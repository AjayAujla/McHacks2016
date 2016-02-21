from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.shortcuts import redirect
from main.models import *

# Create your views here.

def dashboard(request):
	if request.method == 'GET':
		return redirect(index)
	if request.method == 'POST' and request.POST['formType'] == 'create_group':
		user = User.objects.get(user_name = request.POST['username'])
		newGroup = Group()
		newGroup.name = request.POST['group']
		newGroup.save()
		newGroup.users.add(user)
	elif request.method == 'POST' and request.POST['formType'] == 'create_pref':
		user = User.objects.get(user_name = request.POST['username'])
		# If preference doesn't exist, create it
		pref = Preference.objects.filter(name=request.POST['pref'])
		if pref.exists():
			user.preference.add(pref[0])
		else:
			newPref = Preference()
			newPref.name =  request.POST['pref']
			newPref.save()
			user.preference.add(newPref)

	context = {
		'user': user,
		'userAvailability': user.availability.all,
		'userPreferences': user.preference.all,
		'userGroups': Group.objects.filter(users__user_name='Bob')
	}

	return render(request, 'main/dashboard.html', context)

def enter_dashboard(request, user):
	context = {
		'user': user,
		'userAvailability': user.availability.all,
		'userPreferences': user.preference.all,
		'userGroups': Group.objects.filter(users__user_name='Bob')
	}
	return render(request, 'main/dashboard.html', context)

def group(request, group_name):
	try:
		group = Group.objects.get(name=group_name)
	except Group.DoesNotExist:
		raise Http404("Group doesn't exist!")
	users = group.users.all
	if request.method == 'POST' and request.POST['formType'] == 'add_friend':
		# check if friendo exists
		friend = User.objects.filter(user_name=request.POST['friend'])
		if friend.exists():
			group.users.add(friend[0])
	context = {
		'group': group,
		'group_name': group_name,
		'users': users,
	}

	return render(request, 'main/group.html', context)

def register(request):
    if request.method == 'GET':
        # display empty form
        return render(request, 'main/register.html', {})
    elif request.method == 'POST':
        # request is a POST, save user info to database
        newUser = User()
        newUser.user_name = request.POST['user_name']
        newUser.first_name = request.POST['first_name']
        newUser.last_name = request.POST['last_name']
        newUser.postal_code = request.POST['postal_code']
        newUser.password = request.POST['password']
        newUser.save()
        return enter_dashboard(request, newUser)
#    else:
        #TODO: raise 404 or something
def index(request):
    if request.method == 'GET':
		# display empty form
		return render(request, 'main/index.html', {})
    elif request.method == 'POST':
		# request is a POST, try to login
		user = User.objects.filter(user_name=request.POST['username'])
		if user.exists() and user[0].password == request.POST['password']:
			return enter_dashboard(request, user[0])
		else:
			# login unsuccessful
			return render(request, 'main/index.html', { 'message': 'Login unsuccessful' })
