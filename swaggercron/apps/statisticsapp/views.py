from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from .calculation import get_total_income,get_current_year_income,get_upcoming_income,get_period_income_and_difference


@api_view(['GET'])
def getStatistic(request):
     if request:
        data = {
        "total_income": get_total_income(request.user),
        "current_year_income": get_current_year_income(request.user),
        "upcoming_income": get_upcoming_income(request.user)
       }
        return Response(data,status=status.HTTP_200_OK)
    
    


@api_view(['GET'])
def getStatisticSales(request):
     if request:
        data = get_period_income_and_difference(request.user)
        return Response(data,status=status.HTTP_200_OK)


