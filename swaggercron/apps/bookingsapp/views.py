from rest_framework import viewsets
from .serializer import BookingSerializer
from .models import BookingModel
# Create your views here.
class BookingView(viewsets.ModelViewSet):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    def get_queryset(self):
        return self.queryset.filter()
    def perform_update(self, serializer):
        serializer.save()
    def perform_create(self,serializer):
        serializer.save(
        ) 