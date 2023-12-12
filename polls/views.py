from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Person


# Create your views here.


def index(request):
    return HttpResponse("Hello, Aishwarya. You're at the polls index.")


def show(request):
    mydata = Person.objects.all().values()
    template = loader.get_template('show.html')
    context = {
      'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))