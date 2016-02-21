from __future__ import unicode_literals

from django.db import models

# Preferences are more general, eg : outdoors
class Preference(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Availability(models.Model):
    start_date=models.DateTimeField('Available from')
    end_date = models.DateTimeField('Available to')

class User(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=7)
    preference = models.ManyToManyField(Preference)
    availability = models.ManyToManyField(Availability)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user_name

# Activities are a specific event, eg : hiking Mont Royal
class Activity(models.Model):
    name = models.CharField(max_length=50)
    preferences = models.ManyToManyField(Preference)

    def __str__(self):
        return self.name

# For each planned activity, make a "group" to decide what activity and when
class Group(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    chosen_activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='chosen_activity', blank=True, null=True)
    chosen_date = models.ForeignKey(Availability, on_delete=models.CASCADE, related_name='chosen_date', blank=True, null=True)
    suggested_activities = models.ManyToManyField(Activity, related_name='suggested_activities', blank=True, null=True)
    suggested_dates = models.ManyToManyField(Availability, related_name='suggested_dates', blank=True, null=True)

    def __str__(self):
        return self.name

# Candidates belong to group and activity and store voter list
class Candidate_Activity(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    voters = models.ManyToManyField(User)

class Candidate_Availability(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    availability = models.ForeignKey(Availability, on_delete=models.CASCADE)
    voters = models.ManyToManyField(User)
