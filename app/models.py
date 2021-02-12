from django.db import models

class KospiPredict(models.Model):
	name = models.CharField("기업", max_length=20, null=False, default='')
	date = models.DateField("날짜", max_length=10, null=False, unique=True)
	close = models.FloatField("종가", null=True)
	open = models.FloatField("시가", null=True)

	def __str__(self):
		return self.name
