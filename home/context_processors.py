from ast import Sub
from .forms import SubmissionForm

def submissionform(request): 
    return {"submission_form" : SubmissionForm()}