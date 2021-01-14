from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import ImageUploadForm


def index(request, image=None):
    if request.method == 'POST':
        print("POST received")
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid!")
            image = form.cleaned_data['image']
            return HttpResponseRedirect(reverse('image_classification:index', kwargs={'image': image}))

    else:
        form = ImageUploadForm()
        print("GET received")

    if image is not None:
        print("image is not none!")

    context = {
        'form': form,
        'image': image
    }
    return render(request, 'image_classification/index.html', context)
