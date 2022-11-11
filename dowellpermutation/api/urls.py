from django.urls import path

from .views import permutation,save,clear_session

urlpatterns = [

    path('save/', save, name="save"),
    path('calculateperm/', permutation, name="permutations"),
    path('clear_session/', clear_session, name="clear_session"),

]
