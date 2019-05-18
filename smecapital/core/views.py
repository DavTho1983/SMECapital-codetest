from django.contrib.auth import login

from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from Loans.models import Loans
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home(request, start=0, end=10):

    return render(request, 'home.html')


def create_loan():
    return

def home(request):
    loans = Loans.objects.all()

    return render(request, 'home.html', {'loans': loans})
