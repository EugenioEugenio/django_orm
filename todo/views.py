

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Страница списка дел (To-Do List)")
# Create your views here.
