from django import forms
from bootstrap3_datetime.widgets import DateTimePicker

class addEvent(forms.Form):
    title = forms.CharField(
        label='Titolo', max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Titolo'}))
    start_date = forms.DateTimeField(
        label='Data inizio',
        widget=forms.DateTimeInput(attrs={'placeholder': 'GG/MM/AA'}))
    end_date = forms.DateTimeField(
        label='Data fine',
        widget=forms.DateTimeInput(attrs={'placeholder': 'GG/MM/AA'}))
    image = forms.FileField(
        label='Immagine',
        widget=forms.ClearableFileInput(attrs={'placeholder': 'Selezione un file'}))
    description = forms.CharField(
        label='Descrizione', max_length=800,
        widget=forms.TextInput(attrs={'placeholder': 'Descrizione'}))
    price = forms.CharField(
        label='Prezzo', max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Prezzo'}))
    reservation_required = forms.BooleanField(
        label='Prenotazione richiesta',
        widget=forms.CheckboxInput())
    address = forms.CharField(
        label='Indirizzo', max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Indirizzo'}))
    phone_number = forms.CharField(
        label='Numero di telefono', max_length=255,
        widget=forms.TextInput(attrs={'placeholder': '+391234567890'}))
    website = forms.URLField(
        label='Website',
        widget=forms.URLInput(attrs={'placeholder': 'www.website.com'}))
    email = forms.EmailField(
        label='Email', max_length=255,
        widget=forms.EmailInput(attrs={'placeholder': 'address@mail.com'}))
    other = forms.CharField(
        label='Altro', max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Atro'}))
