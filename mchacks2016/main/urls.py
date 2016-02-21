from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^dashboard', views.dashboard, name='dashboard'),				# /dashboard/
	url(r'^register', views.register, name='register'),				# /register/
	url(r'^group/(?P<group_name>\w+)', views.group, name='group'),		# /group/[group_name]/
	url(r'^', views.index, name='index'), 								# /
]
