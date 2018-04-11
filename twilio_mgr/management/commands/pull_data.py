from firebase import firebase
from django.core.management.base import BaseCommand, CommandError
from twilio_mgr.models import SmsNumber, Message, Location, MessageLog
import re
import os


# This will pull the data from firebase
class Command(BaseCommand):
    help = 'Sends confirmation to numbers that have not received one yet'

    # def add_arguments(self, parser):
        # parser.add_argument('poll_id', nargs='+', type=int)

    def pull_data(self):
        # Find these values at https://twilio.com/user/account
        print("Pulling data from Firebase!")
        try:
            firebase_url = os.environ['FIREBASE_URL']
            upcoming_tbd = os.environ['UPCOMING_TBD']

            fb = firebase.FirebaseApplication(firebase_url, None)
            data = fb.get("/phoneReminders", None)


            # Iterate and save this number.
            for key in data:
                d = data[key]
                loc = d['location']
                number = d['phone']
                print(loc)
                if loc is not None:
                    location = Location.objects.get(lat=loc['lat'], lon=loc['lon'])
                else:
                    location = None

                try:
                    smsNumber = SmsNumber.objects.get(sms=number)
                except SmsNumber.DoesNotExist:
                    #create new number
                    smsNumber = SmsNumber(sms=number, location=location, reminder_date=upcoming_tbd, firebase_id=key)
                    smsNumber.save()

            return True
        except Exception as e:
            raise CommandError('Something Happened while processing site %s' % (str(e)))
            return False

        return False


    def handle(self, *args, **options):
        self.pull_data()
