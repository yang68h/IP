from __future__ import unicode_literals

from django.db import models

# Create your models here.
class HostIp(models.Model):
    user=models.CharField(max_length=20)
    ipaddr=models.CharField(max_length=100)
    mac=models.CharField(max_length=100)
