from django.urls import path

from .views import index,permutation,save,clear_session,permutations

urlpatterns = [
    path('',index, name='index'),
    path('save/', save, name="save"),
    path('calculateperm/', permutation, name="permutation"),
    path('clear_session/', clear_session, name="clear_session"),
    path('permutations/', permutations, name="permutations"),
]
