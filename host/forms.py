from django import forms
from models import HostIp
class HostAddr(forms.Form):
    hostUser=forms.CharField(error_messages={'required':u'input username'},
        label=u'username',
        max_length=20,
        required=True)
    hostIpaddr=forms.CharField(
        error_messages={'required':u'input ip address'},
        label=u'ipaddr',
        max_length=100,
        required=True)
    hostMac=forms.CharField(
        error_messages={'required':u'input mac address'},
        label=u'mac-address',
        max_length=100,
        required=True)