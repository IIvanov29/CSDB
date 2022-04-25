from datetime import date
from email import message
from unicodedata import category
from django.shortcuts import render, redirect
from .forms import SubmissionForm
from .models import Submission, Tutorial
from django.contrib import messages      
from django.core.paginator import Paginator
import math


#Function used for saving data from the 'Submission' Model to DB. 
def save_submission(request):
        if request.method == 'POST':
            form = SubmissionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,f'Thank you for your submission, you will be able to see it on our page after it passes a review!')
                return redirect ('/')

def home(request):

    p = Paginator(Submission.objects.all().order_by('-date_submitted'),13)
    page = request.GET.get('page')
    submissions = p.get_page(page) 
    context = {    
        'submissions': submissions,
        'title': 'Home'
    }   
    save_submission(request)


    return render(request, 'csdb_templates/home.html', context,)


def show_submission(request, submission_id):

    submission = Submission.objects.get(pk=submission_id)

    save_submission(request)
    return render(request, 'csdb_templates/submission.html', {'submission': submission})




def learning(request):

    save_submission(request)
    first = False
    context = {
        'title': 'Learning',
        'networking_tutorials':Tutorial.objects.filter(tutorial_category="networking"),
        'networking_tutorials_number':range(0, 3),
        }
    print(math.ceil(Tutorial.objects.count()/2))
    return render(request, 'csdb_templates/learning.html', context)


def networking(request):
    save_submission(request)
    return render(request, 'csdb_templates/learning-networking.html')

def cstools(request):
    save_submission(request)
    return render(request, 'csdb_templates/learning-cstools.html')
    
def programming(request):
    save_submission(request)
    return render(request, 'csdb_templates/learning-programming.html')

def csbasics(request):
    save_submission(request)
    return render(request, 'csdb_templates/learning-csbasics.html')    


def news(request):

    save_submission(request)

    return render(request, 'csdb_templates/news.html', {'title': 'News'})
