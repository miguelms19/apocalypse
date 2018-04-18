from django.shortcuts import render
from airtable import Airtable

Event_Table = Airtable('apptkUXfhIKkSCft0',  # base_id
              'Events', api_key='keyoOFryShWQQ1qGs') #apikey

Date_Table = Airtable('apptkUXfhIKkSCft0',  # base_id
              'Dates', api_key='keyoOFryShWQQ1qGs') #apikey

# Create your views here.
def events(request):
    all_events = Event_Table.get_all()
    print(all_events)
    return render(request, 'booking/event.html', {'all_events':all_events})

def dates(request, event_id ):
    event_dates = Date_Table.get_all()
    print("\nthe dates are\n")
    print(event_dates)
    return render(request, 'booking/dates.html')
