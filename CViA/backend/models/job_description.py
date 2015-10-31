from django.db import models


class JobDescription(models.Model):
	job_title = models.TextField()
	description = models.TextField()
	skills = models.TextField()
	experience = models.TextField()
	education = models.TextField()
	languages = models.TextField()
	location = models.TextField()
