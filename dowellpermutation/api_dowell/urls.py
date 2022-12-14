from django.urls import path

from .views import index, calculateperm, save, calcperm

urlpatterns = [
    path("", index, name="index"),
    path("calculateperm/", calculateperm, name="calculateperm"),
    path("save/", save, name="save"),
    path("calcperm/", calcperm, name="calcperm"),
]
