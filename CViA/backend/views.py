from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], form.title)
            return HttpResponseRedirect('fileuploaded.html')
    else:
        form = UploadFileForm()
    return render_to_response('upload_cv.html', {'form': form})

def handle_uploaded_file(ufile, title):
    with open("resume/{0}".format(title), "wb+") as target:
        for chunk in f.chunks():
            target.write(chunk)

