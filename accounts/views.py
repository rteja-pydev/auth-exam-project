from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserCreationForm
from . import views

# Create your views here.
def home_view(request):
    return render(request, 'home.html')


def guidelines_view(request):
    return render(request, 'guidelines.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

@login_required
def java_view(request):
    return render(request, 'java.html')

@login_required
def python_view(request):
    return render(request, 'python.html')

@login_required
def aptitude_view(request):
    return render(request, 'aptitude.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html',{'form': form})
