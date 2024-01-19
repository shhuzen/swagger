from django.db import models
from apps.toursapp.models import TourModel
# Create your models here.

class BookingModel(models.Model):
    STATUS_FIELD =  [
        ('open', 'open'),
        ('advance', 'advance'),
        ('paid', 'paid'),
    ]
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    tour = models.ForeignKey(TourModel, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_FIELD,max_length=20)
    amount = models.DecimalField(max_digits=15, decimal_places=9)
    advance_amount = models.DecimalField(max_digits=15, decimal_places=9)
    customer_name = models.CharField(max_length=100)
    customer_phonenumber = models.CharField(max_length=100)
    comment = models.TextField()
    adult_travelers_count = models.IntegerField()
    child_travelers_count = models.IntegerField()

    class Meta:
        ordering = ['date']
