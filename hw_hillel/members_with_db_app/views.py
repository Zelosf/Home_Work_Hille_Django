from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm


def input_page(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.user = request.user
                message.save()
                return redirect('display_page')
        else:
            form = MessageForm()
        return render(request, "input_messages_page_db.html", {'form': form})

    else:
        return HttpResponse('You have no permissions to view this page')


def display_page(request):
    try:
        messages = Message.objects.filter(user=request.user).latest('created_at')
    except Message.DoesNotExist:
        messages = None
    return render(request, 'display_messages_page_db.html', {'messages': [messages]})


def all_message_page(request):
    messages = Message.objects.filter(user=request.user).all()

    return render(request, 'display_messages_page_db.html', {'messages': messages})

def members_page(request):
    return render(request, 'members_db.html')
