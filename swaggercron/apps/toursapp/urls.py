from django.urls import path, include,re_path

from rest_framework.routers import DefaultRouter
from .views import TourView,ScheduleView,PictureView

router = DefaultRouter()
router.register("tours", TourView, basename="tours")


urlpatterns = [
    re_path(r'tours/pictures/(?P<pk>\d+)/$', PictureView.as_view({'delete':'destroy'})),
    re_path(r'tours/pictures/$', PictureView.as_view({ 'get': 'list',
    'post': 'create'})),
    re_path(r'tours/(?P<id>[^/.]+)/schedule', ScheduleView.as_view()),
    path('', include(router.urls)),




]

