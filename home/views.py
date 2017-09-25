import json

from django.http import HttpResponse
from django.shortcuts import render

from home.models import Email
from .forms import EmailForm


def home_site(request):
    success = False
    form = EmailForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            #and request.POST.get('agree_check'):
            form.save()
            form = EmailForm()
            success = True

    return render(request, 'index.html', {'form': form, 'success': success})

def privacy_site(request):
    return render(request, 'privacy.html', {})