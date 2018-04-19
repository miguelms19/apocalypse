from django.shortcuts import render
from airtable import Airtable
from datetime import datetime

Event_Table = Airtable('apptkUXfhIKkSCft0',  # base_id
              'Events', api_key='keyoOFryShWQQ1qGs') #apikey

Date_Table = Airtable('apptkUXfhIKkSCft0',  # base_id
              'Dates', api_key='keyoOFryShWQQ1qGs') #apikey

# Create your views here.
def events(request):
    all_events = Event_Table.get_all()
    print("\nthe events are\n")
    print(all_events)

    return render(request, 'booking/event.html', {'all_events': all_events})

def dates(request, event_id ):
    no_dates = 'no dates available'
    # dates = Date_Table.get_all()
    # print(dates)

    events = Event_Table.get_all()
    event_date_id_dic ={}
    for event in events:
        if 'Dates' in event['fields']:
            event_date_id_dic[event['id']] = event['fields']['Dates']
        else:
            event_date_id_dic[event['id']] = [no_dates]

    # print(event_date_id_dic)

    available_event_dates = []
    test_list =[]
    for date_id in event_date_id_dic[event_id]:
        if date_id == no_dates:
            available_event_dates.append(date_id)
        else:
            available_event_dates.append(Date_Table.get(date_id)['fields'].get('Date'))

    print(available_event_dates)

    formated_dates=[]
    if no_dates in available_event_dates:
        # print(available_event_dates)
        return render(request, 'booking/dates.html',{'available_event_dates': available_event_dates})
    else:
        for date in available_event_dates:
            changed_date = datetime.strptime(date,"%Y-%m-%d").strftime("%d/%m/%Y")
            formated_dates.append(changed_date)
        # print(formated_dates)
        sorted_dates = sorted(formated_dates, key=lambda x: datetime.strptime(x, "%d/%m/%Y"))
        # print(sorted_dates)
        return render(request, 'booking/dates.html', {'sorted_dates':sorted_dates})
