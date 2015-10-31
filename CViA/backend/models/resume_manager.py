from django.db import models
import os

from ..CVParser.cv_parser import CVParser


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
