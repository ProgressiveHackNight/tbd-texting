from twilio.rest import Client
import sendgrid
from sendgrid.helpers.mail import *
import os

def twilio_send(number, message):
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
        print('Something Happened while sending message to %s - %s' % (message, str(e)))
        return False

    return False

def sendgrid_send(email, message):

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("Clear Your Cabinet New York <do-not-reply@clearyourcabinet.ag.ny.gov>")
    to_email = Email(email)
    subject = "Thank you for signing up for a take-back reminder."
    content = Content("text/html", message)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    return response
