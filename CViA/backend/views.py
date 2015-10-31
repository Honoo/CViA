from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
import os

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
    with open("{0}/resume/{1}".format(os.path.dirname(os.path.abspath(__file__)), ufile), "wb+") as target:
        for chunk in ufile.chunks():
            target.write(chunk)

def upload_successful(request):
    return render_to_response("file_uploaded.html")

