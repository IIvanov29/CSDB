from datetime import date
from email import message
from django.shortcuts import render, redirect
from .forms import SubmissionForm
from .models import Submission
from django.contrib import messages      
from django.core.paginator import Paginator

def home(request):

    p = Paginator(Submission.objects.all().order_by('-date_submitted'),13)
    page = request.GET.get('page')
    submissions = p.get_page(page) 
    context = {    
        'submissions': submissions,
        'title': 'Home'
    }
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data.get('author_email')
            form.save()
            messages.success(request,f'Thank you for your submission, you will be able to see it on our page after it passes a review!')
            return redirect ('/')

    return render(request, 'csdb_templates/home.html', context,)


def show_submission(request, submission_id):
    submission = Submission.objects.get(pk=submission_id)

    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data.get('author_email')
            form.save()
            messages.success(request,f'Thank you for your submission, you willl be able to see it on our page after it passes a review!')
    return render(request, 'csdb_templates/submission.html', {'submission': submission})




def about(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data.get('author_email')
            form.save()
            messages.success(request,f'Thank you for your submission, you will be able to see it on our page after it passes a review!')
            return redirect ('/about')
    return render(request, 'csdb_templates/about.html', {'title': 'About'})
