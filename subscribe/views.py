from django.shortcuts import render
from Sending_mail.settings import EMAIL_HOST_USER
from subscribe import forms
from django.core.mail import send_mail


# Create your views here.
# DataFlair #Send Email
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Sketch'
        message = 'Hope you are enjoying the mailing service'
        recepient = str(sub['Email'].value())
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form': sub})
