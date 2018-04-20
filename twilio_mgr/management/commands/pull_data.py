from firebase import firebase
from django.core.management.base import BaseCommand, CommandError
from twilio_mgr.models import SmsNumber, Message, Location, MessageLog, EmailReminder
import re
import os


# This will pull the data from firebase
class Command(BaseCommand):
    help = 'Sends confirmation to numbers that have not received one yet'

    # def add_arguments(self, parser):
        # parser.add_argument('poll_id', nargs='+', type=int)

    def pull_mobile_data(self):
        # Find these values at https://twilio.com/user/account
        print("Pulling data from Firebase!")
        try:
            firebase_url = os.environ['FIREBASE_URL']
            upcoming_tbd = os.environ['UPCOMING_TBD']

            # Uncomment once authentiaction is activated
            firebase_secret = os.environ['FIREBASE_SECRET']
            firebase_id = os.environ['FIREBASE_ID']
            firebase_email = os.environ['FIREBASE_EMAIL']
            authentication = firebase.FirebaseAuthentication(firebase_secret, firebase_email, extra={'id': firebase_id})
            fb = firebase.FirebaseApplication(firebase_url, authentication=authentication)
            # fb = firebase.FirebaseApplication(firebase_url, None)
            data = fb.get("/phoneReminders", None)

            print(data)
            if data is None:
                print("No Data")
            else:
                # Iterate and save this number.
                for key in data:
                    d = data[key]
                    number = d['phone']

                    if 'location' in d and d['location'] is not None and d['location'] != '':
                        loc = d['location']
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
            raise CommandError('Something Happened while processing site - %s' % (str(e)))
            return False

        return False


    def pull_email_data(self):
        # Find these values at https://twilio.com/user/account
        print("Pulling data from Firebase!")
        try:
            firebase_url = os.environ['FIREBASE_URL']
            upcoming_tbd = os.environ['UPCOMING_TBD']

            # Uncomment once authentiaction is activated
            firebase_secret = os.environ['FIREBASE_SECRET']
            firebase_id = os.environ['FIREBASE_ID']
            firebase_email = os.environ['FIREBASE_EMAIL']
            authentication = firebase.FirebaseAuthentication(firebase_secret, firebase_email, extra={'id': firebase_id})
            fb = firebase.FirebaseApplication(firebase_url, authentication=authentication)
            # fb = firebase.FirebaseApplication(firebase_url, None)
            data = fb.get("/emailReminders", None)

            if data is None:
                print("No email data")
            else:
                # Iterate and save this number.
                for key in data:
                    print("Getting %s " % key)
                    d = data[key]

                    print(d)

                    email = d['email']
                    if 'location' in d and d['location'] is not None and d['location'] != '':
                        loc = d['location']
                        location = Location.objects.get(lat=loc['lat'], lon=loc['lon'])
                    else:
                        location = None


                    try:
                        emailReminder = EmailReminder.objects.get(email=email, location=location)
                    except EmailReminder.DoesNotExist:
                        #create new number
                        emailReminder = EmailReminder(email=email, location=location, reminder_date=upcoming_tbd, firebase_id=key)
                        emailReminder.save()

            return True
        except Exception as e:
            raise CommandError('Something Happened while processing site - %s' % (str(e)))
            return False

        return False


    def handle(self, *args, **options):
        self.pull_mobile_data()
        self.pull_email_data()
