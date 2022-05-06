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
            else:
                messages.warning(request,f'Verification Failure, please try again!')
                print("NO")
                return redirect('/')
def home(request):

    p = Paginator(Submission.objects.filter(is_approved=True).order_by('-date_submitted'),10)
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
        }
    return render(request, 'csdb_templates/learning.html', context)


def networking(request):
    save_submission(request)
    networking_tutorials_p = Paginator(Tutorial.objects.filter(tutorial_category="networking").order_by('-tutorial_date_posted'),10)
    networking_tutorials_page = request.GET.get('page')
    networking_tutorials = networking_tutorials_p.get_page(networking_tutorials_page) 

    return render(request, 'csdb_templates/learning-networking.html', {'networking_tutorials': networking_tutorials} )    

def cstools(request):
    save_submission(request)
    cstools_tutorials_p = Paginator(Tutorial.objects.filter(tutorial_category="cstools").order_by('-tutorial_date_posted'),10)
    cstools_tutorials_page = request.GET.get('page')
    cstools_tutorials = cstools_tutorials_p.get_page(cstools_tutorials_page) 

    return render(request, 'csdb_templates/learning-cstools.html', {'cstools_tutorials': cstools_tutorials} )    
    
def programming(request):
    save_submission(request)
    programming_tutorials_p = Paginator(Tutorial.objects.filter(tutorial_category="programming").order_by('-tutorial_date_posted'),10)
    programming_tutorials_page = request.GET.get('page')
    programming_tutorials = programming_tutorials_p.get_page(programming_tutorials_page) 

    return render(request, 'csdb_templates/learning-programming.html', {'programming_tutorials': programming_tutorials} )    

def csbasics(request):
    save_submission(request)
    csbasics_tutorials_p = Paginator(Tutorial.objects.filter(tutorial_category="csbasics").order_by('-tutorial_date_posted'),10)
    csbasics_tutorials_page = request.GET.get('page')
    csbasics_tutorials = csbasics_tutorials_p.get_page(csbasics_tutorials_page) 

    return render(request, 'csdb_templates/learning-csbasics.html', {'csbasics_tutorials': csbasics_tutorials} )    

def tutorial(request, tutorial_id):
    tutorial = Tutorial.objects.get(pk=tutorial_id)

    return render(request,'csdb_templates/tutorial.html', {'tutorial':tutorial})



def news(request):

    save_submission(request)

    return render(request, 'csdb_templates/news.html', {'title': 'News'})


def forum(request):
    save_submission(request)

    return render(request, 'csdb_templates/forum.html', {'title':'Forum'})

def privacy(request):
    save_submission(request)

    return render(request, 'csdb_templates/privacy.html', {'title':'Privacy Policy'})
