from django.http import HttpResponse
from django.shortcuts import render

def greeting(request):
    # context holds the variables we want pass into the template
    context = {'name': 'Otto'}

    # render handles rendering the template and placing it in a HttpResponse
    return render(request, 'greeting.html', context)
