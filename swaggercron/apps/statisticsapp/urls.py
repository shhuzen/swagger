from django.urls import path,re_path


from .views import getStatistic,getStatisticSales

urlpatterns = [
    re_path('statistics/$',getStatistic ),
        path('statistics/sales/',getStatisticSales ),

]
