from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
	count = User.objects.count()
	return render(request, 'home.html', {
		'count': count
	})


def companies(request):
	return render(request, 'companies.html')


def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserCreationForm()

	return render(request, 'registration/signup.html', {
		'form': form
	})


@login_required
def profile(request):
	return render(request, 'profile.html')


def read_more(request):
	return render(request, 'profile.html')


def dev_profile(request):
	return render(request, 'devprofile.html')


def technology(request):
	return render(request, 'technology.html')


def customer(request):
	return render(request, 'customer.html')


def hr(request):
	return render(request, 'hr.html')


def admi(request):
	return render(request, 'admi.html')


def editprofile(request):
    if request.method == 'POST':
        if request.POST.get('headline') and request.POST.get('content'):
            post=Post()
            post.title= request.POST.get('title')
            post.content= request.POST.get('content')
            post.save()
            return render(request, 'editprofile.html')  
    else:
            return render(request,'editprofile.html')
