from django.urls import path

from .views import *

urlpatterns = [
    path('', index_view, name="IndexView"),
    path('desktop/2', desktop_two_view, name="DesktopTwoView"),
    path('desktop/3', desktop_three_view, name="DesktopThreeView"),
]
