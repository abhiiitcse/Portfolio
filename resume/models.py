from django.db import models
from django.utils import timezone

class Project(models.Model):
	title = models.CharField(max_length = 600)
	intro = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.title

