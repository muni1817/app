from django.shortcuts import render

from django.http import HttpResponse

def muni(request):
    return HttpResponse('<h1>muni</h1>')
