from django.shortcuts import render
from water.models import WaterReading
from water.serializers import WaterReadingSerializer
from rest_framework import viewsets


class WaterReadingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = WaterReading.objects.all().order_by('-date')
    serializer_class = WaterReadingSerializer
