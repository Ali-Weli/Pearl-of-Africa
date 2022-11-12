from django.shortcuts import render
from django.http import HttpResponse# new
from django.template import loader#new



def index(request):
    return render(request, 'entries/index.html')

    template = loader.get_template('entries/index.html')
    context = {}
    return HttpResponse(template.render(context, request)) 

def add(request):
     return render(request, 'entries/add.html')
