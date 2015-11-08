import os
import json
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .forms import UploadFileForm, JobDescriptionForm, CVForm
from .models import Resume, JobDescription

def index(request):
    return HttpResponse("Hello World")

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            messages.add_message(request, messages.SUCCESS, 'CV successfully uploaded.')
            return HttpResponseRedirect('../job_list')
    else:
        form = UploadFileForm()
    return render_to_response('upload_cv.html', {'form': form})

def handle_uploaded_file(ufile):
    filename = "{0}/resume/{1}".format(os.path.dirname(os.path.abspath(__file__)), ufile)
    with open(filename, "wb+") as target:
        for chunk in ufile.chunks():
            target.write(chunk)
    Resume.objects.create_from_pdf(filename)

def upload_successful(request):
    return render_to_response("file_uploaded.html")

@csrf_exempt
def input_job_description(request):
    if request.method == 'POST':
        form = JobDescriptionForm(request.POST)
        if form.is_valid():
            handle_job_description(form)
            messages.add_message(request, messages.SUCCESS, 'Job description successfully saved.')
            return HttpResponseRedirect('../job_list')
    else:
        form = JobDescriptionForm()
    return render_to_response('job_description.html', {'form': form})

def handle_job_description(form):
    data = form.cleaned_data
    job_desc = JobDescription(
        job_title=data['job_title'], 
        description = data['description'],
        skills = data['skills'],
        experience = data['experience'],
        education = data['education'],
        languages = data['languages'],
        location = data['location'],
        skills_weightage = data['skills_weightage'],
        experience_weightage = data['experience_weightage'],
        education_weightage = data['education_weightage'],
        languages_weightage = data['languages_weightage']
        )
    job_desc.save()

def job_success(request):
    return render_to_response("input_successful.html")

def get_job_descriptions(request):
    job_desc = JobDescription.objects.all()
    data = serializers.serialize("json", job_desc)
    return HttpResponse(data, content_type='application/json')

def edit_job_description(request, pk):
    job_desc = get_object_or_404(JobDescription, pk=pk)
    if request.method == 'POST':
        form = JobDescriptionForm(request.POST)
        if form.is_valid():
            update_job_description(form, pk)
            messages.add_message(request, messages.SUCCESS, 'Job description successfully updated.')
            return HttpResponseRedirect('../../')
    
    else :    
        form = JobDescriptionForm(initial={
                                    'job_title': job_desc.job_title,
                                    'description' : job_desc.description,
                                    'location' : job_desc.location,
                                    'skills' : job_desc.skills,
                                    'skills_weightage' : job_desc.skills_weightage,
                                    'experience' : job_desc.experience,
                                    'experience_weightage' : job_desc.experience_weightage,
                                    'education' : job_desc.education,
                                    'education_weightage': job_desc.education_weightage,
                                    'languages': job_desc.languages,
                                    'languages_weightage': job_desc.languages_weightage
                                    })
    return render(request, "edit_job_description.html", {'form': form})

def update_job_description(form, pk):
    data = form.cleaned_data
    job_desc = JobDescription.objects.filter(pk=pk).update(
        job_title=data['job_title'], 
        description = data['description'],
        skills = data['skills'],
        experience = data['experience'],
        education = data['education'],
        languages = data['languages'],
        location = data['location'],
        skills_weightage = data['skills_weightage'],
        experience_weightage = data['experience_weightage'],
        education_weightage = data['education_weightage'],
        languages_weightage = data['languages_weightage']
        )


def job_list(request):
    return render_to_response("description_list.html", context_instance=RequestContext(request))

def job_match(request):
    context = {} 
    return render(request, 'job_matcher.html', context)

def get_cvs(request):
    cvs = Resume.objects.all()
    data = serializers.serialize("json", cvs)
    return HttpResponse(data, content_type='application/json')

def cv_list(request):
    return render_to_response("cv_list.html", context_instance=RequestContext(request))

def edit_cv(request):
    cv = get_object_or_404(Resume, pk=pk)
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            update_cv(form, pk)
            messages.add_message(request, messages.SUCCESS, 'CV successfully updated.')
            return HttpResponseRedirect('../../')
    
    else :    
        form = CVForm(initial={
                    'name' : cv.name,
                    'email' : cv.email,
                    'phone' : cv.phone,
                    'skills' : cv.skills,
                    'experience' : cv.experience,
                    'education' : cv.education,
                    'awards' : cv.awards,
                    'honors' : cv.honors,
                    'languages' : cv.languages,
                    'personal_references' : cv.personal_references,
                    'interest' : cv.interest,
                    'technology' : cv.technology,
                    'certification' : cv.certification,
                    'projects' : cv.projects,
                    'summary' : cv.summary,
                    'objective' : cv.objective 
                    })
    
    return render(request, "edit_cv.html", {'form': form})

def update_cv(form, pk):
    data = form.cleaned_data
    cv = Resume.objects.filter(pk=pk).update(
            name = data['name'],
            email = data['email'],
            phone = data['phone'],
            skills = data['skills'],
            experience = data['experience'],
            education = data['education'],
            awards = data['awards'],
            honors = data['honors'],
            languages = data['languages'],
            personal_references = data['personal_references'],
            interest = data['interest'],
            technology = data['technology'],
            certification = data['certification'],
            projects = data['projects'],
            summary = data['summary'],
            objective = data['objective'],
        )
