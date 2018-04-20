from django.http import HttpResponse
from django.shortcuts import render
from airtable import Airtable

Gallery_Table = Airtable('appZJXumNCOFemo8r',  # base_id
              'Gallery Page', api_key='keyoOFryShWQQ1qGs') #apikey

def home(request):
    return render(request, 'home.html')

def addevent(request):
    return render(request, 'admin/addevent.html')

def skirmish(request):
    return render(request, 'skirmish.html')

def gallery(request):

    all_gallery_images = Gallery_Table.get_all()
    # print(all_gallery_images)
    return render(request, 'gallery.html', {'all_gallery_images': all_gallery_images})
