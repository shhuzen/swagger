
from django.db.models import Sum
from datetime import datetime,timedelta
from apps.bookingsapp.models import BookingModel
from apps.toursapp.models import TourModel


def get_total_income(user):
    total_income = BookingModel.objects.filter(tour__profile__user=user,status='paid').aggregate(total_income=Sum('amount')).get('total_income') or 0  
    return total_income 

def get_current_year_income(user):
    current_year = datetime.now().year
    current_year_income = BookingModel.objects.filter(tour__profile__user=user,status='paid',date__year=current_year).aggregate(current_year_income=Sum('amount')).get('current_year_income') or 0  
    return current_year_income 

def get_upcoming_income(user):
    today = datetime.now().date()
    upcoming_income = BookingModel.objects.filter(tour__profile__user=user,status='open',date__gt=today).aggregate(upcoming_income=Sum('amount')).get('upcoming_income') or 0  
    upcoming_income += BookingModel.objects.filter(tour__profile__user=user,status='advance',date__gt=today).aggregate(upcoming_income=Sum('amount')).get('upcoming_income') or 0  
    return upcoming_income

def get_period_income_and_difference(user):
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)
    bookings = BookingModel.objects.filter(tour__profile__user=user,date__range=[week_ago, today])
    booking_ids = bookings.values_list('tour_id', flat=True)
    tours = TourModel.objects.filter(id__in=booking_ids)
    results = []
    for tour in tours:
        income = bookings.filter(tour=tour).aggregate(total_income=Sum('amount')).get('total_income', 0)
        income_difference = bookings.filter(tour=tour,status='paid').count() - bookings.filter(tour=tour,status='advance').count()
        results.append({'name':tour.name,
                        "period_income": income,
        "period_income_difference": income_difference})
    data = {
        "count": bookings.count()-1,
        "results": results
    }

    return data
