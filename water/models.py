from django.db import models

# Create your models here.
class WaterReading(models.Model):
	date = models.DateTimeField(auto_now_add=True, blank=True)
	reading = models.FloatField(default=0.0, blank=True, null=True)

	def __str__(self):
		return f"Date: {0}, Reading: {1}".format(self.date, self.reading)