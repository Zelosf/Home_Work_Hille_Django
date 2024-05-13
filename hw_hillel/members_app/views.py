from django.http import HttpResponse
from django.shortcuts import render


def input_page(request):
    return render(request, "input_messages_page.html")

def display_page(request):

    message = {'messages': request.POST.get("message")}
    request.session['messages'] = message
    return render(request, 'display_messages_page.html', message)


def session_page(request):
    messages = request.session.get("messages")
    return render(request, 'display_messages_page.html', messages)


def members_page(request):
    return render(request, 'members.html')