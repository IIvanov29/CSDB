from django.contrib import admin
from home.models import Submission, Tutorial
# Register your models here.

class SubmissionAdmin(admin.ModelAdmin):
    exclude = ('tc_consent',)
    readonly_fields = ('author_email','author_name','vuln_type','vuln_title','vuln_description','vuln_attachments','date_submitted')
    date_hierarchy = 'date_submitted'


class TutorialAdmin(admin.ModelAdmin):
    readonly_fields = ('tutorial_date_posted',)

admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Tutorial, TutorialAdmin)