from django.db import models

class Project(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	homepage = models.CharField(max_length=200)
	source_url = models.CharField(max_length=200)
