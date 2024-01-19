from django.db import models
from django.core.validators import MinValueValidator

from apps.accountsapp.models import ProfileModel
class TourModel(models.Model):
    types = [
        ('group', 'group'),
        ('individual', 'individual'),
     ]
    
    name = models.CharField(max_length=200,null=True)
    type = models.CharField(choices=types, max_length=255,null=True)
    duration = models.IntegerField(null=True)
    child_price = models.FloatField(max_length=10,null=True)
    adult_price = models.FloatField(max_length=10,null=True)
    way_to_travel = models.ForeignKey('WayToTravelModel',on_delete=models.DO_NOTHING,null=True)
    age_limit = models.IntegerField(null=True)
    gathering_place = models.TextField(null=True)
    gatherring_place_location = models.TextField(null=True)
    route_description = models.TextField(null=True)
    what_is_included = models.TextField(null=True)
    what_is_not_included = models.TextField(null=True)
    profile = models.ForeignKey(ProfileModel,on_delete=models.CASCADE,null=True)

class PictureModel(models.Model):
    tourkey = models.ForeignKey('TourModel',on_delete=models.CASCADE,null=True,related_name='pictures')
    image = models.ImageField(upload_to='media/accounts/pictures/',null=True,blank=True)

class LocationModel(models.Model):
    tourkey = models.ForeignKey('TourModel',on_delete=models.CASCADE,null=True,related_name='locations')
    order = models.IntegerField(validators=[MinValueValidator(0)],null=True)
    description = models.TextField(null=True)
    
class ScheduleModel(models.Model):
    tour = models.ForeignKey('TourModel',on_delete=models.CASCADE,blank=True,null=True,related_name='schedule')
    
class WayToTravelModel(models.Model):
    name = models.CharField(max_length=200,null=True)

class WeekModel(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    name = models.CharField(choices=DAYS_OF_WEEK, max_length=255,null=True)
    from_time = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
    to_time = models.DateTimeField( auto_now=False, auto_now_add=False,null=True)
    schedulekey = models.ForeignKey('ScheduleModel',on_delete=models.CASCADE,null=True,related_name='week')

class NonsheduleddatesModel(models.Model):
    schedulekey = models.ForeignKey('ScheduleModel',on_delete=models.CASCADE,null=True,related_name='non_sheduled_dates')
    date = models.DateField(auto_now=False, auto_now_add=False,null=True)
    from_time = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
    to_time = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
