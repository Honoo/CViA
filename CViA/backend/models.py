from django.db import models

# Create your models here.

class Resume(models.Model):
	class Meta:
		managed = False # directly references the SQL
		db_table = "resume"
	pid = models.PositiveIntegerField(primary_key=True, db_column="id")
	name = models.CharField(db_column="name")
	email = models.CharField(db_column="email")
	phone = models.CharField(db_column="phone")
	skills = models.TextField(db_column="skills")
	experience = models.TextField(db_column="experience")
	education = models.TextField(db_column="education")
	awards = models.TextField(db_column="awards")
	languages = models.TextField(db_column="languages")
	personal_references = models.TextField(db_column="personal_references")
	interests = models.TextField(db_column="interests")

class JobDescription(models.Model):
	class Meta:
		managed = False
		db_table = "job_description"
	pid = models.PositiveIntegerField(primary_key=True, db_column="id")
	job_title = models.TextField(db_column="job_title")
	description = models.TextField(db_column="description")
	skills = models.TextField(db_column="skills")
	experience = models.TextField(db_column="experience")
	education = models.TextField(db_column="education")
	languages = models.TextField(db_column="languages")
	location = models.TextField(db_column="location")

class Weightage(models.Model):
	class Meta:
		managed = False
		db_table = "weightage"
	pid = models.PositiveIntegerField(primary_key=True, db_column="id")
	job_description_id = models.PositiveIntegerField(db_column="job_description_id")
	skills_weightage = models.FloatField(db_column="skills_weightage")
	education_weightage = models.FloatField(db_column="education_weightage")
	languages_weightage = models.FloatField(db_column="languages_weightage")
	experience_weightage = models.FloatField(db_column="experience_weightage")