from typing import List
from rest_framework.views import APIView
from rest_framework.response import Response

from shuffle.functions import final_shuffle
from django.views.generic import TemplateView
from rest_framework import serializers

class IndexView(TemplateView):
    template_name = 'index.html'


class SeriesSerializer(serializers.Serializer):
    M = serializers.ListField(min_length=1, required=True)
    n = serializers.IntegerField(min_value=1, required=True)
    r = serializers.IntegerField(min_value=1, required=True)
    
    # validate n
    def validate_n(self, value):
        if 'M' not in self.initial_data:
            raise serializers.ValidationError("M is missing")
        if value > len(self.initial_data['M']):
            raise serializers.ValidationError("n should be less than the length of M")
        return value
    
    # validate r
    def validate_r(self, value):
        if 'n' not in self.initial_data:
            raise serializers.ValidationError("n is missing")
        if value > self.initial_data['n']:
            raise serializers.ValidationError("r should be less than n")
        return value
    
    
class Shuffler(APIView):
    def post(self, request):
        # get the serialized input series
        serializer = SeriesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # get the series
        series = serializer.validated_data['M']
        
        # get n
        n = serializer.validated_data['n']
        
        # get r
        r = serializer.validated_data['r']
        
        items, result = final_shuffle(series, n, r)
        
        response = {"selected_items": items,  "permuted_items": result}
        return Response(response)

