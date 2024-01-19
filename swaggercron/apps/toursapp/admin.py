from django.contrib import admin
from .models import TourModel,PictureModel,LocationModel,WeekModel,ScheduleModel,NonsheduleddatesModel,WayToTravelModel


admin.site.register([TourModel,PictureModel,LocationModel,
                     WeekModel,ScheduleModel,
                     NonsheduleddatesModel,WayToTravelModel])