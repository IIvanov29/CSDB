from django.shortcuts import render

posts =[
    {
        'author':'Ivelin Ivanov 2',
        'title':'SQL Injections',
        'type': 'Web Application',
        'content':'SQL Injections in a nutshell',
        'date_posted':'04/12/2022',
    },
    {
        'author':'IIvanov2',
        'title': 'SQL Injections2',
        'type': 'Web Application',
        'content': 'SQL Injections in a nutshell',
        'date_posted': '05/12/2022',
    },
    {
        'author':'IIvanov2',
        'title': 'SQL Injections2',
        'type': 'Web Application',
        'content': 'SQL Injections in a nutshell',
        'date_posted': '06/12/2022',
    },
     {
        'author':'IIvanov2',
        'title': 'SQL Injections2',
        'type': 'Web Application',
        'content': 'SQL Injections in a nutshell',
        'date_posted': '06/12/2022',
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
