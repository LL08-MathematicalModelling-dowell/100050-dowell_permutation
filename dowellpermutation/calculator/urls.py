from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('home/', home, name="home"),

    path('permutations/select/', permutataionselect, name="permutataionselect"),
    path('calcpermutations/', calcpermutations, name="calcpermutations"),

    path('permutations/save/', save, name="save"),
    path('clear_session/', clear_session, name="clear_session"),
    path('calculateperm/', calculateperm, name="calculateperm"),

]
