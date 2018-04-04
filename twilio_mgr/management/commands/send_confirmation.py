from twilio.rest import Client
from django.core.management.base import BaseCommand, CommandError
from twilio_mgr.models import SmsNumber, Message, Location, MessageLog
import re
import os


# This is all in compliance of FCC Regulations
# Source: http://blog.textit.in/ensuring-your-sms-messaging-service-complies-with-fcc-regulations-tcpa
WELCOME_MESSAGE_KEY = 'WELCOME_MESSAGE'

class Command(BaseCommand):
    help = 'Sends confirmation to numbers that have not received one yet'

    # def add_arguments(self, parser):
        # parser.add_argument('poll_id', nargs='+', type=int)

    def twilio_send(self, number, message):
        # Find these values at https://twilio.com/user/account
        account_sid = os.environ['TWILIO_API_KEY']
        auth_token = os.environ['TWILIO_SECRET_KEY']
        source_number = os.environ['TWILIO_SOURCE_NUMBER']

        print("%s - %s " % (account_sid, auth_token))
        try:
            client = Client(account_sid, auth_token)
            print("client")
            client.api.account.messages.create(
                to=number,
                from_=source_number,
                body=message)
            print(client.http_client.last_response.status_code)
            return True
        except Exception as e:
            raise CommandError('Something Happened while sending message to %s - %s' % (message, str(e)))
            return False

        return False


    def handle(self, *args, **options):
        targets = SmsNumber.objects.filter(cancelled=False, sent_intro=False)
        message = Message.objects.get(keyword=WELCOME_MESSAGE_KEY);

        for sms in targets:
            try:

                # Prepare Message
                true_msg = re.sub('\[ADDRESS\]', sms.location.address, message.message)
                self.stdout.write(self.style.SUCCESS('Sending Message "%s" to "%s"' % (true_msg, sms.sms)))

                # 1. Send Message Twilio
                self.twilio_send(sms.sms, true_msg)

                # 2. Mark SMS as intro'd
                sms.sent_intro = True
                sms.reminder_sent = False
                sms.save()

                # 3. Save Message to Message Log
                message_log = MessageLog(sms_number=sms, message=true_msg)
                message_log.save()

                self.stdout.write(self.style.SUCCESS('Successfully sent intro "%s"' % sms.id))

            except Exception as e:
                raise CommandError('Something Happened while sending message to %s - %s' % (sms.sms, str(e)))
