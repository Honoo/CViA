import os
import json
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .forms import UploadFileForm
from .forms import JobDescriptionForm
from .models import Resume
from .models import JobDescription

def index(request):
    return HttpResponse("Hello World")

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('../upload_successful')
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
            return HttpResponseRedirect('../job_success')
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
    job_desc = get_object_or_404(Question, pk=pk)
    return render(request, "edit_job_description.html", {"job": job_desc})

def job_list(request):
    return render_to_response("description_list.html")

def job_match(request):
    context = {} 
    return render(request, 'job_matcher.html', context)
