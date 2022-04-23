from email import message
from django.shortcuts import render, redirect
from .forms import SubmissionForm
from .models import Submission
from django.contrib import messages      

def home(request):
    context = {    
        'submissions': Submission.objects.all(),
        'title': 'Home'
    }
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data.get('author_email')
            form.save()
            messages.success(request,f'Thank you for your submission, please confirm it on {email} !')
            return redirect ('/')

    return render(request, 'csdb_templates/home.html', context,)

def about(request):
    return render(request, 'csdb_templates/about.html', {'title': 'About'})
