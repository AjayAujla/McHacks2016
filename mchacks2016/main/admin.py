from django.contrib import admin
from main.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Preference)
admin.site.register(Availability)
admin.site.register(Activity)
admin.site.register(Group)
admin.site.register(Candidate_Activity)
admin.site.register(Candidate_Availability)