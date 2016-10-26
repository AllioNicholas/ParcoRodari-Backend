from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    creation_date = timezone.now()
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField('start date and time of the event')
    end_date = models.DateTimeField('end date and time of the event')
    image = models.FileField(upload_to='images/{}'.format(id), null=True)
    description = models.CharField(max_length=800)
    price = models.CharField(max_length=255, null=True)
    reservation_required = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    other = models.CharField(max_length=255, null=True)

    def create_event(title, start_date, end_date, image, description, price, reservation_required, address, phone_number, website, email, other):
        new_event = Event(title=title, start_date=start_date, end_date=end_date, image=image,
                        description=description, price=price, reservation_required=reservation_required,
                        address=address, phone_number=phone_number, website=website, email=email, other=other)
        return new_event

    def __str__(self):
        return self.title
