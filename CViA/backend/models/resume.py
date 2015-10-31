from django.db import models

from .resume_manager import ResumeManager


class Resume(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	skills = models.TextField()
	experience = models.TextField()
	education = models.TextField()
	awards = models.TextField()
	honors = models.TextField()
	languages = models.TextField()
	personal_references = models.TextField()
	interests = models.TextField()
	technology = models.TextField()
	certification = models.TextField()
	projects = models.TextField()
	summary = models.TextField()
	objective = models.TextField()

	objects = ResumeManager()
