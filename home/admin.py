from django.contrib import admin
from home.models import Submission
# Register your models here.

class SubmissionAdmin(admin.ModelAdmin):
    exclude = ('tc_consent',)
    readonly_fields = ('author_email','author_name','vuln_type','vuln_title','vuln_description','vuln_attachments','date_submitted')
    date_hierarchy = 'date_submitted'
admin.site.register(Submission, SubmissionAdmin)