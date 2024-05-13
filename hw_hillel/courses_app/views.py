from django.http import HttpResponse
from django.shortcuts import render

#Determining whether the user is authorized or not
def authenticated(request):
    user = {
        'is_authenticated': request.user.is_authenticated
    }
    return render(request, 'authenticated_message.html', user)