from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Event


def index(request):
    return HttpResponse("Hello, world. You're at the events index.")

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', {'event': event})

def index(request):
    events = get_list_or_404(Event)
    return render(request, 'events/index.html', {'event_list': events})

def edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/edit.html', {'event': event})
