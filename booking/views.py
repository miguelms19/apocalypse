from django.shortcuts import render
from airtable import Airtable

Event_Table = Airtable('apptkUXfhIKkSCft0',  # base_id
              'Events', api_key='keyoOFryShWQQ1qGs') #apikey

Date_Table = Airtable('apptkUXfhIKkSCft0',  # base_id
              'Dates', api_key='keyoOFryShWQQ1qGs') #apikey

# Create your views here.
def events(request):
    all_events = Event_Table.get_all()
    return render(request, 'booking/event.html', {'all_events':all_events})

def dates(request):
    pass
