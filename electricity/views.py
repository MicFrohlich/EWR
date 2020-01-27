from django.shortcuts import render
from electricity.models import ElectricalReading
from electricity.serializers import ElectricalReadingSerializer
from rest_framework import viewsets


class ElectricalReadingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ElectricalReading.objects.all().order_by('-date')
    serializer_class = ElectricalReadingSerializer
