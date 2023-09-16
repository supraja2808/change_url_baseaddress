from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def data_from_url(request,name):
    return HttpResponse('hello{}'.format(name))
