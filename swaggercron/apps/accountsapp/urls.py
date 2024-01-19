from django.urls import path, include


from .views import Login,ProfileView

urlpatterns = [
    path('login/',Login),
    path('profile/', ProfileView.as_view()),
]
