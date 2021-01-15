import base64

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import ImageUploadForm


def index(request):
    image_uri = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # passing the image as base64 string to avoid storing it to DB or filesystem
            image = form.cleaned_data['image']
            encoded_img = base64.b64encode(image.file.read()).decode('ascii')
            image_uri = 'data:%s;base64,%s' % ('image/jpeg', encoded_img)

    else:
        form = ImageUploadForm()

    context = {
        'form': form,
        'image_uri': image_uri,
    }
    return render(request, 'image_classification/index.html', context)
