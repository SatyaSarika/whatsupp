from django import forms
from messenger.models import *
from django.forms import Textarea

class MessageForm(forms.ModelForm):
    class Meta(object):
        model=Message
        exclude=['fromuser','touser']
        widgets = {
            'chattext': Textarea(attrs={'cols': 50, 'rows': 4}),
        }