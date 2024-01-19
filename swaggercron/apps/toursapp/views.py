from rest_framework import viewsets,generics
from .models import ScheduleModel, TourModel,PictureModel
from .serializer import TourSerializer,ScheduleSerializer,PictureSerializer
from django.shortcuts import get_object_or_404
from apps.accountsapp.models import ProfileModel
# Create your views here.
class TourView(viewsets.ModelViewSet):
    queryset = TourModel.objects.all()
    serializer_class = TourSerializer
    def get_queryset(self):
            return self.queryset.filter(profile__user=self.request.user)

    def perform_update(self, serializer):
        profile = ProfileModel.objects.get(user=self.request.user)
        serializer.save(profile=profile)

    def perform_create(self, serializer):
        profile = ProfileModel.objects.get(user=self.request.user)
        serializer.save(profile=profile)
# Просто появляються фотки но можно их привязать к туру
# Но я не нашел как по апи смотрел логики никакой 
# не id не pk просто tours/pictures/ 
# если так то можно было many to many сделать 
#в итоге решил то что в бади попадает по нему понимать какой 
class PictureView(viewsets.ModelViewSet):
    queryset = PictureModel.objects.all()
    serializer_class = PictureSerializer
    def get_queryset(self):
            return self.queryset.filter()
    def perform_update(self, serializer):
            serializer.save()
    def perform_create(self,serializer):

            serializer.save(tourkey_id=self.request.data.get("tour")
            ) 
            
class ScheduleView(generics.RetrieveUpdateAPIView
):
   serializer_class = ScheduleSerializer
   queryset = ScheduleModel.objects.all()
   def get_object(self):
    queryset = self.get_queryset()
    obj = queryset.filter(tour_id=self.kwargs['id']).first()
    if obj:
      return obj
    else:
        create = ScheduleModel.objects.create(tour_id=self.kwargs['id'])
        create.save()
        obj = get_object_or_404(queryset,tour_id=self.kwargs['id'])
    return obj

   def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

