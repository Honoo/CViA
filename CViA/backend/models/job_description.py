from django.db import models
from .resume import Resume
from ..JobMatcher import JobMatcher


class JobDescription(models.Model):
	job_title = models.TextField()
	description = models.TextField()
	skills = models.TextField()
	experience = models.FloatField()
	education = models.TextField()
	languages = models.TextField()
	location = models.TextField()

	skills_weightage = models.FloatField(default=1L)
	education_weightage = models.FloatField(default=1L)
	languages_weightage = models.FloatField(default=1L)
	experience_weightage = models.FloatField(default=1L)

	@property
	def weights(self):
		attributes = ['skills', 'education', 'languages', 'experience']
		total_weights = 0.0
		for attr in attributes:
			total_weights += getattr(self, attr+'_weightage')
		weights = {}
		for attr in attributes:
			if total_weights <= 0.001:
				weights[attr] = 1.0 / len(attributes)
			else:
				weights[attr] = getattr(self, attr+'_weightage') / total_weights
		return weights

	def match_all(self):
		matcher = JobMatcher(self.__dict__, weights=self.weights)
		resumes = Resume.objects.all()
		scores = [matcher.score(r.__dict__) for r in resumes]
		return sorted(scores, key=lambda v: v['score']['total'], reverse=True)