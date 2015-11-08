from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class JobDescriptionForm(forms.Form):
    job_title = forms.CharField(label='Job Title')
    description = forms.CharField(label='Description')
    location = forms.CharField(label='Location')
    skills = forms.CharField(label='Skills')
    skills_weightage = forms.FloatField()
    experience = forms.CharField(label='Years of Experience')
    experience_weightage = forms.FloatField()
    education = forms.CharField(label='Education')
    education_weightage = forms.FloatField()
    languages = forms.CharField(label='Languages')
    languages_weightage = forms.FloatField()
    
    
