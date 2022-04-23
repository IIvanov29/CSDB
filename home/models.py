from pickle import TRUE
from typing_extensions import Required
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Submission(models.Model):
    date_sumbmitted = models.DateTimeField(auto_now=True)
    author_email = models.EmailField()
    author_name = models.CharField(max_length=24)
    vuln_type = models.CharField(max_length=24)
    vuln_title = models.CharField(max_length=24)
    vuln_description = models.TextField(max_length=200)
    vuln_attachments = models.FileField()
    tc_consent = models.BooleanField()
