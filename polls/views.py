from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def index(request):
    return HttpResponse("Hello, Aishwarya. You're at the polls index.")


def show(request):
    return HttpResponse("Hello, Aishwarya. You're at the polls page.")