from django.urls import path

from .views import *

urlpatterns = [
    path('', index_view, name="IndexView"),
    path('desktop/2', desktop_two_view, name="DesktopTwoView"),
    path('desktop/3', desktop_three_view, name="DesktopThreeView"),
    path('permutations/select', desktop_four_view, name="permutation"),
    path('desktop/5', desktop_five_view, name="DesktopFiveView"),
    path('desktop/6', desktop_six_view, name="DesktopSixView"),
    path('desktop/7', desktop_seven_view, name="DesktopSevenView"),
    path('permutations/', permutations, name="permutations")
]
