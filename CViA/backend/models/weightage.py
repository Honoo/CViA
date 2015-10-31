from django.db import models

from .job_description import JobDescription


class Weightage(models.Model):
	job_description = models.ForeignKey(JobDescription)
	skills_weightage = models.FloatField()
	education_weightage = models.FloatField()
	languages_weightage = models.FloatField()
	experience_weightage = models.FloatField()
