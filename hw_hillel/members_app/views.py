from django.http import HttpResponse
from django.shortcuts import render


def input_page(request):
    return HttpResponse("INPUT")

def display_page(request):
    return HttpResponse("Display")

def session_page(request):
    return HttpResponse("session")

def members_page(request):
    return render(request, 'members.html')