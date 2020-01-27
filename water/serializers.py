from water.models import WaterReading
from rest_framework import serializers


class WaterReadingSerializer(serializers.ModelSerializer):
	class Meta:
		model = WaterReading
		fields = ["date", "reading"]