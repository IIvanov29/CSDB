from pickle import TRUE
from typing_extensions import Required
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Submission(models.Model):
    date_submitted = models.DateTimeField(blank=True, default=timezone.now)
    author_email = models.EmailField()
    author_name = models.CharField(max_length=24)
    vuln_type = models.CharField(max_length=24)
    vuln_title = models.CharField(max_length=24)
    vuln_description = models.TextField(max_length=200)
    vuln_attachments = models.FileField()
    is_approved = models.BooleanField(blank=True)  

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length = 50)
    tutorial_author = models.CharField(max_length=24)
    tutorial_category = models.CharField(max_length = 200,choices=[("cstools", 'Cyber Sec Tools'), ("networking", 'Networking'),("csbasics", 'Cyber Security Basics'),("programming", 'Programming')])
    tutorial_description_text = models.TextField(default=None)
    tutorial_video_link = models.URLField(blank=True)
    tutorial_date_posted = models.DateTimeField(blank=True, default=timezone.now)
