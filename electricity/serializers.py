from electricity.models import ElectricalReading
from rest_framework import serializers


class ElectricalReadingSerializer(serializers.ModelSerializer):
	class Meta:
		model = ElectricalReading
		fields = ["date", "reading"]