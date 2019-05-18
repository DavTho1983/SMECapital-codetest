from django.contrib.auth import login

from Loans.models import Loans
from django.shortcuts import render

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

def home(request):
    loans = Loans.objects.all()

    return render(request, 'home.html', {'loans': loans})
