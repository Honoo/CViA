from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def upload_cv(request):
    return HttpResponse("Hello, world.")