from django.urls import path
from shuffle.views import IndexView, Shuffler

urlpatterns = [
    path('api/', Shuffler.as_view()),
    path('', IndexView.as_view(), name='index'),
]
