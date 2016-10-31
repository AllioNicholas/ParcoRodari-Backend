from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import views as auth_views, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.urlresolvers import reverse
from .models import Event
from .forms import addEvent

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

def add(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            # if there is a GET request to the url render the form
            add_event_form = addEvent()
            return render(request, 'events/add.html',
                      {'add_event_form': add_event_form,
                       'button': 'Aggiungi evento'})
        elif request.method == 'POST':
            add_event_form = addEvent(request.POST)
            if add_event_form.is_valid():
                title = add_event_form.cleaned_data['title']
                start_date = add_event_form.cleaned_data['start_date']
                end_date = add_event_form.cleaned_data['end_date']
                image = request.FILES['image']
                description = add_event_form.cleaned_data['description']
                price = add_event_form.cleaned_data['price']
                reservation_required = add_event_form.cleaned_data['reservation_required']
                address = add_event_form.cleaned_data['address']
                phone_number = add_event_form.cleaned_data['phone_number']
                website = add_event_form.cleaned_data['website']
                email = add_event_form.cleaned_data['email']
                other = add_event_form.cleaned_data['other']
                new_event = Event.create_event(title=title, start_date=start_date,
                            end_date=end_date, image=image, description=description,
                            price=price, reservation_required=reservation_required,
                            address=address, phone_number=phone_number, website=website,
                            email=email, other=other)
                new_event.save()
                messages.success(request, 'Event added successfully!')
                return HttpResponseRedirect(reverse('/events/'))
            else:
                # there is invalid data!
                return render(request, 'events/add.html',
                              {'add_event_form': add_event_form,
                               'button': 'Aggiungi evento'})
    else:
        return HttpResponseRedirect('/login/')
