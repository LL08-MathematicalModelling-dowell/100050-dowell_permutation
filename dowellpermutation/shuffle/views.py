from typing import List
from rest_framework.views import APIView
from rest_framework.response import Response

from shuffle.functions import final_shuffle

# views.py
from django.views.generic import TemplateView
from rest_framework import serializers

class IndexView(TemplateView):
    template_name = 'index.html'
# Create your views here.
class SeriesSerializer(serializers.Serializer):
    series = serializers.ListField(min_length=1)
class Shuffler(APIView):
    def post(self, request):
        # get the serialized input series
        serializer = SeriesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # get the series
        series = serializer.validated_data['series']
        
        result = final_shuffle(series)
        
        response = {'result': result}
        return Response(response)

