from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    tpl = render_to_string('twilio_mgr/index.html')
    return HttpResponse(tpl)

    # Create Captcha
    # Insert Number + Zipcode
