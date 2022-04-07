from django.shortcuts import render

posts =[
    {
        'author':'IIvanov',
        'title':'SQL Injections',
        'content':'SQL Injections in a nutshell',
        'date_posted':'April, 7, 2022',
    },
    {
        'author':'IIvanov2',
        'title': 'SQL Injections2',
        'content': 'SQL Injections in a nutshell',
        'date_posted': 'April, 8, 2022',
    }
]

        


def home(request):
    context = {
        'posts':posts,
        'title': 'Home'
    }
    return render(request, 'csdb_templates/home.html', context,)

def about(request):
    return render(request, 'csdb_templates/about.html', {'title': 'About'})
