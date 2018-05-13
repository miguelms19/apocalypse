from django.http import HttpResponse
from django.shortcuts import render
from airtable import Airtable
from datetime import datetime

Gallery_Table = Airtable('appZJXumNCOFemo8r',  # base_id
                         'Gallery Page', api_key='keyoOFryShWQQ1qGs')  # apikey
Blog_Table = Airtable('appf9kdwo9dS1DiM8',
                      'Blog', api_key='keyoOFryShWQQ1qGs')
Commandpost_Table = Airtable('appZJXumNCOFemo8r',
                             'Command Post', api_key='keyoOFryShWQQ1qGs')
Village_Table = Airtable('appZJXumNCOFemo8r',
                         'Village', api_key='keyoOFryShWQQ1qGs')
SafeZone_Table = Airtable('appZJXumNCOFemo8r',
                          'Safe Zone', api_key='keyoOFryShWQQ1qGs')
OutliningStuff_Table = Airtable('appZJXumNCOFemo8r',
                                'Outlining Stuff', api_key='keyoOFryShWQQ1qGs')
Trenches_Table = Airtable('appZJXumNCOFemo8r',
                          'Trenches', api_key='keyoOFryShWQQ1qGs')
Under18_Table = Airtable('appZJXumNCOFemo8r',
                         'Under 18', api_key='keyoOFryShWQQ1qGs')


def home(request):
    return render(request, 'home.html')


def venue(request):
    return render(request, 'venue.html')


def airsoft(request):
    return render(request, 'whatisairsoft.html')


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
        changed_date = datetime.strptime(blog['fields']['Date'], "%Y-%m-%d").strftime("%B %d, %Y")
        # print(changed_date)
        sorted_blogs.append((blog['fields']['Date'], changed_date, blog['fields']['Heading'],
                             blog['fields']['Text'], blog['fields']['Head_Image'],
                             blog['id']))

    sorted_blogs.sort(reverse=True)
    print(sorted_blogs)

    return render(request, 'blog.html', {'sorted_blogs': sorted_blogs})


def eachblog(request, blog_id):
    blog_detail = Blog_Table.get(blog_id)
    # print(blog_detail)

    blog_date = Blog_Table.get(blog_id)['fields']['Date']
    changed_date_format = datetime.strptime(blog_date, "%Y-%m-%d").strftime("%B %d, %Y")
    # print(changed_date_format)

    return render(request, 'eachblog.html', {'blog_detail': blog_detail,
                                             'changed_date_format': changed_date_format})


def gallery(request):
    '''commented out the code as we do not need the sorting on gallery Page now'''
    # all_gallery_images = Gallery_Table.get_all()
    # gallery = []
    # for images in all_gallery_images:
    #     gallery.append((images['createdTime'], images['fields']['Event'], images['fields']['Images']))
    # gallery.sort(reverse=True)
    # return render(request, 'gallery.html', {'gallery': gallery})
    return render(request, 'gallery.html')


def gallery_sort(table_data):
    sorted_gallery = []

    for images in table_data:
        if 'Images' in images['fields'].keys():
            sorted_gallery.append((images['fields']['Number'], images['fields']['Images']))

    sorted_gallery.sort(reverse=True)
    return sorted_gallery


def commandpost_gallery(request):
    all_command_images = Commandpost_Table.get_all()
    cp_gallery = gallery_sort(all_command_images)
    return render(request, 'commandpostgallery.html', {'cp_gallery': cp_gallery})


def village_gallery(request):
    all_village_images = Village_Table.get_all()
    village_gallery = gallery_sort(all_village_images)
    return render(request, 'villagegallery.html', {'village_gallery': village_gallery})


def safezone_gallery(request):
    all_safezone_images = SafeZone_Table.get_all()
    safezone_gallery = gallery_sort(all_safezone_images)
    return render(request, 'safezonegallery.html', {'safezone_gallery': safezone_gallery})


def outlining_gallery(request):
    all_outlining_images = OutliningStuff_Table.get_all()
    outlining_gallery = gallery_sort(all_outlining_images)
    return render(request, 'outlininggallery.html', {'outlining_gallery': outlining_gallery})


def trenches_gallery(request):
    trenches_data = Trenches_Table.get_all()
    trenches_gallery = gallery_sort(trenches_data)
    return render(request, 'trenchesgallery.html', {'trenches_gallery': trenches_gallery})


def under18_gallery(request):
    under18_data = Under18_Table.get_all()
    under18_gallery = gallery_sort(under18_data)
    return render(request, 'under18gallery.html', {'under18_gallery': under18_gallery})
