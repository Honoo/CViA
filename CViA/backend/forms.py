from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit

class UploadFileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        helper = FormHelper()

        helper.form_action = './'
        helper.form_method = 'POST'
        helper.attrs = {'enctype': 'multipart/form-data'}
        helper.add_input(Submit('submit', 'Upload CV'))

        self.helper = helper
        super(UploadFileForm, self).__init__(*args, **kwargs)

    file = forms.FileField(label='')

class JobDescriptionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        helper = FormHelper()

        helper.form_action = './'
        helper.form_class = 'form-horizontal'
        helper.form_method = 'POST'
        helper.attrs = {'enctype': 'multipart/form-data'}
        helper.label_class = 'col-lg-2'
        helper.field_class = 'col-lg-10'
        helper.layout = Layout(
            "job_title",
            "description",
            "location",
            Div(
                Div("skills", css_class="col-lg-8"),
                Div("skills_weightage", css_class="col-lg-4"),
                css_class="row",
            ),
            Div(
                Div("experience", css_class="col-lg-8"),
                Div("experience_weightage", css_class="col-lg-4"),
                css_class="row",
            ),
            Div(
                Div("education", css_class="col-lg-8"),
                Div("education_weightage", css_class="col-lg-4"),
                css_class="row",
            ),
            Div(
                Div("languages", css_class="col-lg-8"),
                Div("languages_weightage", css_class="col-lg-4"),
                css_class="row",
            ),
        )
        helper.add_input(Submit('submit', 'Submit'))

        self.helper = helper
        super(JobDescriptionForm, self).__init__(*args, **kwargs)

    job_title = forms.CharField(label='Job Title')
    description = forms.CharField(label='Description', widget=forms.Textarea)
    location = forms.CharField(label='Location')
    skills = forms.CharField(label='Skills')
    skills_weightage = forms.FloatField(label='Weight', required=False)
    experience = forms.CharField(label='Years of Experience')
    experience_weightage = forms.FloatField(label='Weight', required=False)
    education = forms.CharField(label='Education')
    education_weightage = forms.FloatField(label='Weight', required=False)
    languages = forms.CharField(label='Languages', required=False)
    languages_weightage = forms.FloatField(label='Weight', required=False)

class CVForm(forms.Form):
    def __init__(self, *args, **kwargs):
        helper = FormHelper()

        helper.form_action = './'
        helper.form_class = 'form-horizontal'
        helper.form_method = 'POST'
        helper.attrs = {'enctype': 'multipart/form-data'}
        helper.label_class = 'col-lg-2'
        helper.field_class = 'col-lg-10'
        helper.add_input(Submit('submit', 'Submit'))

        self.helper = helper
        super(CVForm, self).__init__(*args, **kwargs)

    name = forms.CharField(label='Name')
    email = forms.CharField(label='Email')
    phone = forms.CharField(label='Phone', required=False)
    skills = forms.CharField(label='Skills', required=False)
    experience = forms.CharField(label='Experience', widget=forms.Textarea, required=False)
    education = forms.CharField(label='Education', required=False)
    awards = forms.CharField(label='Awards', required=False)
    honors = forms.CharField(label='Honors', required=False)
    languages = forms.CharField(label='languages', required=False)
    personal_references = forms.CharField(label='Personal References', widget=forms.Textarea, required=False)
    interests = forms.CharField(label='Interests', required=False)
    technology = forms.CharField(label='Technology', required=False)
    certification = forms.CharField(label='Certification', required=False)
    projects = forms.CharField(label='Projects', widget=forms.Textarea, required=False)
    summary = forms.CharField(label='Summary', widget=forms.Textarea, required=False)
    objective = forms.CharField(label='Objective', widget=forms.Textarea, required=False)
