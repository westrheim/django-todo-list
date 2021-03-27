from django.shortcuts import render
from django.http import HttpResponse




def task_list(request):
    return HttpResponse('To Do list')

def index(request):
    return HttpResponse('Hello friends!')


def test_view(request):
    return HttpResponse('Here is some more stuff')