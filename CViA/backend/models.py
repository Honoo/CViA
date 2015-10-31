from django.db import models

# Create your models here.

class Resume(models.Model):
	# pid = models.PositiveIntegerField(primary_key=True, )
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

class JobDescription(models.Model):
	job_title = models.TextField()
	description = models.TextField()
	skills = models.TextField()
	experience = models.TextField()
	education = models.TextField()
	languages = models.TextField()
	location = models.TextField()

class Weightage(models.Model):
	job_description = models.ForeignKey(JobDescription)
	skills_weightage = models.FloatField()
	education_weightage = models.FloatField()
	languages_weightage = models.FloatField()
	experience_weightage = models.FloatField()