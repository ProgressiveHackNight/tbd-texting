from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import re

# Create your models here.
class Location(models.Model):
    # city= models.CharField(max_length=200, null=True)
    # country = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    hours = models.CharField(max_length=200, blank=True, null=True)
    address =  models.CharField(max_length=400, blank=True, null=True)
    notes = models.CharField(max_length=800, blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "%s (%f, %f)" % (self.address, self.lat, self.lon)

class SmsNumber(models.Model):

    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=200, null=True, blank=True)
    sent_intro = models.BooleanField(default=False)
    cancelled=models.BooleanField(default=False)
    sms = models.CharField(max_length=50)
    notes = models.CharField(max_length=200, blank=True, null=True)
    reminder_sent=models.BooleanField(default=False)
    reminder_date=models.DateTimeField(null=True, blank=True, default=None)
    firebase_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.sms)

class EmailReminder(models.Model):

    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=200, null=True, blank=True)
    sent_intro = models.BooleanField(default=False)
    cancelled=models.BooleanField(default=False)
    email = models.EmailField(max_length=100)
    notes = models.CharField(max_length=200, blank=True, null=True)
    reminder_sent=models.BooleanField(default=False)
    reminder_date=models.DateTimeField(null=True, blank=True, default=None)
    firebase_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.email)


class Message(models.Model):
    message = models.CharField(max_length=1500)
    keyword = models.CharField(max_length=100,unique=True)


    def __str__(self):
        return "%s: %s" % (self.keyword, self.message)

class MessageLog(models.Model):
    sms_number = models.CharField(max_length=300, null=True, blank=True) #models.ForeignKey(SmsNumber, null=True, on_delete=models.SET_NULL)
    email = models.CharField(max_length=300, null=True, blank=True)
    message = models.CharField(max_length=1500, null=True)
    date_sent = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "[%s - %s]\t%s" % (self.sms_number.sms, self.date_sent, self.message)

# Cleaning the sms
@receiver(pre_save, sender=SmsNumber)
def clean_sms(sender, instance, *args, **kwargs):
    instance.sms = re.sub('[^\d]', '', str(instance.sms))
