from rest_framework import serializers
from .models import BookingModel
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = '__all__' 