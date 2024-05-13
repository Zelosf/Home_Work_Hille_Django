from django.http import HttpResponse
from django.shortcuts import render


def input_page(request):
    return render(request, "input_messages_page.html")

def display_page(request):

    messages = {
        'messages': request.POST.get("message")
    }
    return render(request, 'display_messages_page.html', messages)


def session_page(request):
    return HttpResponse("session")

def members_page(request):
    return render(request, 'members.html')