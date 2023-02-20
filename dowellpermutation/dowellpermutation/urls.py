from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', lambda request: redirect('calculator/home/', permanent=True)),
    path("calculator/", include("calculator.urls")),
    path("api/", include("api.urls")),
    path('permutationapi/', include('Permutations_API.urls')),
]
