from django.shortcuts import render, get_object_or_404, redirect
from .models import GovtEvent
#new views code 
from django.shortcuts import render, redirect
from .forms import GovtEventForm

# Create your views here.

def Success_Page(request):
    return render(request, 'success_page.html')

def event_list(request):
    events = GovtEvent.objects.all()
    return render(request, 'govt_event/event_list.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = GovtEventForm(request.POST, request.FILES)
        if form.is_valid():
            # Get cleaned data from the form
            parliament_instance = form.cleaned_data.get('parliament')

            # Ensure parliament_instance is not None before using it
            if parliament_instance is not None:
                # Set the parliament field before saving
                form.instance.parliament = parliament_instance
                form.save()
                return redirect('event_list')
            else:
                print("Parliament field is required.")
        else:
            print(form.errors)
    else:
        form = GovtEventForm()

    return render(request, 'govt_event/create_event.html', {'form': form})


def edit_event(request, event_id):
    # Retrieve the event instance to be edited
    event = get_object_or_404(GovtEvent, id=event_id)

    if request.method == 'POST':
        # Update the form instance with the new data
        form = GovtEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        # Populate the form with the current event data
        form = GovtEventForm(instance=event)

    return render(request, 'govt_event/edit_event.html', {'form': form, 'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(GovtEvent, pk=event_id)
    event.delete()
    return redirect('event_list')  