from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import views as auth_views, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.urlresolvers import reverse
from .models import Event

def main(request):
    return render(request, 'events/main.html', {})

def login(request, *args, **kwargs):
    if request.method == 'POST':
        if 'remember_me' not in request.POST:
            request.session.set_expiry(0)
    return auth_views.login(request, *args, **kwargs)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

@ensure_csrf_cookie
def detail(request, event_id):
    if request.user.is_authenticated():
        event = get_object_or_404(Event, pk=event_id)
        return render(request, 'events/detail.html', {'event': event})
    else:
        return HttpResponseRedirect('/login/')

@ensure_csrf_cookie
def events(request):
    if request.user.is_authenticated():
        events = get_list_or_404(Event)
        return render(request, 'events/list.html', {'event_list': events})
    else:
        return HttpResponseRedirect('/login/')

@ensure_csrf_cookie
def edit(request, event_id):
    if request.user.is_authenticated():
        event = get_object_or_404(Event, pk=event_id)
        return render(request, 'events/edit.html', {'event': event})
    else:
        return HttpResponseRedirect('/login/')

@ensure_csrf_cookie
def add(request):
    if request.user.is_authenticated():
        return render(request, 'events/add.html', {})
    else:
        return HttpResponseRedirect('/login/')
