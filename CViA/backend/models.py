import os

from django.db import models
from CVParser.cv_parser import CVParser


class ResumeManager(models.Manager):
	def import_from_pdf(self, path):
		if not os.path.isabs(path):
			path = os.path.os.path.abspath(path)
		resume_content = CVParser.parse_and_get_content(path)
		resume = self.model()
		for field, value in resume_content.iteritems():
			if hasattr(resume, field):
				setattr(resume, field, value)
		return resume

	def create_from_pdf(self, path):
		resume = self.import_from_pdf(path)
		resume.save()
		return resume

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
