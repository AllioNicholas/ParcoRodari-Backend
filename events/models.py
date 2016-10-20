from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    creation_date = timezone.now()
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date and time of the event')
    end_date = models.DateTimeField('end date and time of the event')
    image = models.FileField(upload_to='images/{}'.format(id), null=True)
    description = models.CharField(max_length=800)
    price = models.CharField(max_length=200, null=True)
    reservation_required = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200, null=True)
    website = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    other = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
