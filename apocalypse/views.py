from django.http import HttpResponse
from django.shortcuts import render
from airtable import Airtable
from datetime import datetime

Gallery_Table = Airtable('appZJXumNCOFemo8r',  # base_id
              'Gallery Page', api_key='keyoOFryShWQQ1qGs') #apikey
Blog_Table = Airtable('appf9kdwo9dS1DiM8',
                'Blog', api_key='keyoOFryShWQQ1qGs')
Commandpost_Table= Airtable('appZJXumNCOFemo8r',
                'Command Post', api_key='keyoOFryShWQQ1qGs')
Village_Table = Airtable('appZJXumNCOFemo8r',
                                'Village', api_key='keyoOFryShWQQ1qGs')


def home(request):
    return render(request, 'home.html')

def addevent(request):
    return render(request, 'admin/addevent.html')

def uploadpic(request):
    return render(request, 'admin/uploadpic.html')

def addblog(request):
    return render(request, 'admin/addblog.html')

def skirmish(request):
    return render(request, 'skirmish.html')

def under18(request):
    return render(request, 'under18.html')

def milsim(request):
    return render(request, 'milsim.html')

def bookings(request):
    return render(request, 'bookings.html')

def blog(request):
    all_blogs = Blog_Table.get_all()
    # print(all_blogs)

    sorted_blogs = []
    for blog in all_blogs:
        changed_date = datetime.strptime(blog['fields']['Date'],"%Y-%m-%d").strftime("%B %d, %Y")
        # print(changed_date)
        sorted_blogs.append((blog['fields']['Date'],changed_date, blog['fields']['Heading'],
                            blog['fields']['Text'], blog['fields']['Head_Image'],
                            blog['id']))

    sorted_blogs.sort(reverse=True)
    print(sorted_blogs)

    return render(request, 'blog.html', {'sorted_blogs':sorted_blogs})


def eachblog(request, blog_id):
    blog_detail = Blog_Table.get(blog_id)
    # print(blog_detail)

    blog_date = Blog_Table.get(blog_id)['fields']['Date']
    changed_date_format = datetime.strptime(blog_date,"%Y-%m-%d").strftime("%B %d, %Y")
    # print(changed_date_format)

    return render(request, 'eachblog.html',{'blog_detail': blog_detail,
                                                'changed_date_format': changed_date_format})

def gallery(request):

    all_gallery_images = Gallery_Table.get_all()
    gallery = []
    for images in all_gallery_images:
        gallery.append((images['createdTime'], images['fields']['Event'], images['fields']['Images']))
    gallery.sort(reverse=True)
    return render(request, 'gallery.html', {'gallery': gallery})
    # return render(request, 'gallery.html', {'all_gallery_images': all_gallery_images})


def commandpost_gallery(request):
    all_command_images = Commandpost_Table.get_all()
    cp_gallery = []
    for images in all_command_images:
        if 'One-Image' in images['fields'].keys():
            cp_gallery.append((images['fields']['Number'],
            images['fields']['One-Image'][0]['url']))
    cp_gallery.sort(reverse=True)
    # print(cp_gallery)
    return render(request, 'commandpostgallery.html', {'cp_gallery':cp_gallery})

def village_gallery(request):
    all_village_images = Village_Table.get_all()
    village_gallery = []
    for images in all_village_images:
        if 'One-Image' in images['fields'].keys():
            village_gallery.append((images['fields']['Number'],
            images['fields']['One-Image'][0]['url']))
    village_gallery.sort(reverse=True)
    # print(village_gallery)
    return render(request, 'villagegallery.html', {'village_gallery':village_gallery})
