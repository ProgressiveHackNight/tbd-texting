from .models import Message
from django import forms

class MessageModelForm( forms.ModelForm ):
    message = forms.CharField( widget=forms.Textarea )
    keyword = forms.CharField( disabled = True)

    class Meta:
        model = Message
        fields = '__all__'
