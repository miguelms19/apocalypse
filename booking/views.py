from django.shortcuts import render
from airtable import Airtable

Event_Table = Airtable('apptkUXfhIKkSCft0',  # base_id
              'Events', api_key='keyoOFryShWQQ1qGs') #apikey

Date_Table = Airtable('apptkUXfhIKkSCft0',  # base_id
              'Dates', api_key='keyoOFryShWQQ1qGs') #apikey

# Create your views here.
def events(request):
    all_events = Event_Table.get_all()
    print("\nthe events are\n")
    print(all_events)
    list_of_events = []
    for event in all_events:
        list_of_events.append((event['fields']['Order'], event['fields']['Event'],
                    event['fields']['Price'], event['fields']['Event_Image'][0]['url'],
                    event['fields']['Description'],event['id']))

    sorted_events = sorted(list_of_events)
    print("\nthe events are\n")
    print(sorted_events)
    return render(request, 'booking/event.html', {'sorted_events':sorted_events})

def dates(request, event_id ):
    event_dates = Date_Table.get_all()
    print("\nthe dates are\n")
    print(event_dates)
    return render(request, 'booking/dates.html')
