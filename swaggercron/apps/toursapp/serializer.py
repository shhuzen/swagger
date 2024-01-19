from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import TourModel,PictureModel

from rest_framework import serializers
from .models import TourModel, PictureModel, LocationModel, ScheduleModel, WeekModel, NonsheduleddatesModel


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = ('order','description')  


class WeekSerializer(serializers.ModelSerializer):
    from_time = serializers.DateTimeField(input_formats=['%H:%M'], format='%H:%M')
    to_time = serializers.DateTimeField(input_formats=['%H:%M'], format='%H:%M')
    class Meta:
        model = WeekModel
        read_only_field = ('id','schedulekey')
        fields = ('name','to_time','from_time') 

class NonSheduledDatesSerializer(serializers.ModelSerializer):
    date = serializers.DateField(input_formats=['%Y-%m-%d'], format='%Y-%m-%d')
    from_time = serializers.DateTimeField(input_formats=['%H:%M'], format='%H:%M')
    to_time = serializers.DateTimeField(input_formats=['%H:%M'], format='%H:%M')
    class Meta:
        model = NonsheduleddatesModel
        read_only_field = ('id','schedulekey')
        fields = ('date','to_time','from_time')  




class ScheduleSerializer(serializers.ModelSerializer):
    week = WeekSerializer(many=True)
    non_sheduled_dates = NonSheduledDatesSerializer(many=True)

    class Meta:
        model = ScheduleModel
        exclude = ('id',)
    def update(self, instance, validated_data):
        week_data = validated_data.pop('week', [])
        non_sheduled_dates_data = validated_data.pop('non_sheduled_dates', [])
        instance = super().update(instance, validated_data)
        self._update_nested_fields(instance.week, week_data, WeekModel)
        self._update_nested_fields(instance.non_sheduled_dates, non_sheduled_dates_data,NonsheduleddatesModel)
        return instance

    def _update_nested_fields(self, instance, data, model):
        instance.clear()

        for item_data in data:
            item_id = item_data.get('id')
            if item_id:
                item = model.objects.get(id=item_id)
                for attr, value in item_data.items():
                    setattr(item, attr, value)
                item.save()
                instance.add(item)
            else:
                item = model.objects.create(**item_data)
                instance.add(item)
                
class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PictureModel
        fields = ['image','id']
        
        
class TourSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True,read_only=True)  
    locations = LocationSerializer(many=True)  
    schedule = ScheduleSerializer(many=True,read_only=True) 
    class Meta:
        model = TourModel
        read_only_fields =('id',)
        exclude = ('profile',)
    def create(self, validated_data):
        validated_data_Location = validated_data.pop('locations',None)
        instance = TourModel.objects.create(**validated_data)
        LocationObjectCreated = LocationModel.objects.create(tourkey=instance,order=validated_data_Location[0].get('order'),
                                                        description=validated_data_Location[0].get('description'))
        return instance

    def update(self, instance, validated_data):
        locations_data = validated_data.pop('locations', [])
        instance= super().update(instance, validated_data)
        self._update_nested_fields(instance.locations, locations_data, LocationModel)
        return instance
    
    def _update_nested_fields(self, instance, data, model):
        instance.clear()
        for item_data in data:
            item_id = item_data.get('id')
            if item_id:
                item = model.objects.get(id=item_id)
                for attr, value in item_data.items():
                    setattr(item, attr, value)
                item.save()
                instance.add(item)
            else:
                item = model.objects.create(**item_data)
                instance.add(item)
    # def validate_pictures(self, value):
    #     min_pictures = 3
    #     max_pictures = 6

    #     if len(value) < min_pictures or len(value) > max_pictures:
    #         raise serializers.ValidationError(f'Количество фоток должно быть больше {min_pictures} и меньше {max_pictures}')

    #     return value



