
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Tent
from django.contrib.auth.decorators import user_passes_test
from .forms import TentForm, SignupForm
from django.contrib.auth.decorators import login_required



def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



def is_superuser(user):
    return user.is_superuser

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Change 'home' to your desired redirect URL
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})





def logout_view(request):
    logout(request)
    return redirect('home') 






# Create your views here.
def home(requst):
    return render(requst, 'home.html')


def tents_view(request):
    tents = Tent.objects.all()
    return render(request, 'tents.html', {'tents': tents})

def tent_detail_view(request, pk):
    tent = get_object_or_404(Tent, pk=pk)
    return render(request, 'tent_detail.html', {'tent': tent})    

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def add_tent(request):
    if request.method == 'POST':
        form = TentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tents')  # Redirect to a list of tents or another page
    else:
        form = TentForm()
    return render(request, 'add_tent.html', {'form': form})    
@user_passes_test(is_superuser)
def tent_edit(request, pk):
    tent = get_object_or_404(Tent, pk=pk)
    if request.method == "POST":
        form = TentForm(request.POST, request.FILES, instance=tent)
        if form.is_valid():
            form.save()
            return redirect('tent_detail', pk=tent.pk)
    else:
        form = TentForm(instance=tent)
    return render(request, 'tent_edit.html', {'form': form})    