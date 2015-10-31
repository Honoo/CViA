from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm
from .models import Resume

def index(request):
    return HttpResponse("Hello World")

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('fileuploaded.html')
    else:
        form = UploadFileForm()
    return render_to_response('upload_cv.html', {'form': form})

def handle_uploaded_file(ufile):
    filename = "resume/{0}".format(ufile)
    with open(filename, "wb+") as target:
        for chunk in f.chunks():
            target.write(chunk)
    Resume.create_from_pdf(filename)

