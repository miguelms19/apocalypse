from django.http import HttpResponse
from django.shortcuts import render
from airtable import Airtable

Gallery_Table = Airtable('appZJXumNCOFemo8r',  # base_id
              'Gallery Page', api_key='keyoOFryShWQQ1qGs') #apikey

def home(request):
    return render(request, 'home.html')

def addevent(request):
    return render(request, 'admin/addevent.html')

def uploadpic(request):
    return render(request, 'admin/uploadpic.html')

def skirmish(request):
    return render(request, 'skirmish.html')

def milsim(request):
    return render(request, 'milsim.html')

def gallery(request):

    all_gallery_images = Gallery_Table.get_all()
    gallery = []
    for images in all_gallery_images:
        gallery.append((images['createdTime'], images['fields']['Event'], images['fields']['Images']))
    gallery.sort(reverse=True)
    return render(request, 'gallery.html', {'gallery': gallery})
    # return render(request, 'gallery.html', {'all_gallery_images': all_gallery_images})
