from django.contrib import admin

# Register your models here.
from .models import SmsNumber, Location, Message, MessageLog
from .forms import MessageModelForm

class MessageAdmin( admin.ModelAdmin ):
    form = MessageModelForm

    def has_add_permission(self, request):
        return False

class MessageLogAdmin( admin.ModelAdmin ):
    def has_add_permission(self, request):
        return False;
    def has_edit_permission(self, request):
        return False


admin.site.register(SmsNumber)
admin.site.register(Location)
admin.site.register(Message, MessageAdmin)
admin.site.register(MessageLog, MessageLogAdmin)
