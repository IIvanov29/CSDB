from typing_extensions import Required
from xml.dom.minidom import Attr
from django import forms
from .models import Submission
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class SubmissionForm(forms.ModelForm):
    vuln_attachments = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'type':'file', 'id':'formfile', 'class':'form-control','multiple':'True'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    class Meta:
        model=Submission
        fields = '__all__'
        widgets = {
            'author_email':forms.EmailInput(attrs={'placeholder':'e.g youremail@email.com', 'class':'form-control', 'id':'email'}),
            'author_name':forms.TextInput(attrs={'placeholder':'e.g IIvanov', 'class':'form-control', 'id':'name'}),
            'vuln_type':forms.TextInput(attrs={'placeholder':'e.g Injections', 'class':'form-control', 'id':'type'}),
            'vuln_title':forms.TextInput(attrs={'placeholder':'e.g SQL Injection', 'class':'form-control', 'id':'title'}),
            'vuln_description':forms.Textarea(attrs={'placeholder':'Use this space to describe your findings...', 'class':'form-control', 'style':'resize:none;','id':'description_text'}),
        }




