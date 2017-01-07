from pprint import pprint
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.db.models import Q
from django import forms
from django.core.exceptions import ValidationError

def index(request):
	context = {
		"Message" 	: 	"Welcome. Please login.",
		"Type"		:	"Default"
	}	
	
	return render(request, 'static/login.html', context)

def login_user(request):
	username = request.POST['username']
	password = request.POST['password']

	user = User.objects.filter(Q(username=username) | Q(email=username))

	if user.count() is not 0:
		user = authenticate(username=user[0].username, password=password)
	else:
		context = {
			"Message" 	: 	"User doesn't exist",
			"Type"		:	"Error"
		}	
		return render(request, 'static/login.html', context)
	
	if user is not None:	
		login(request, user)
		return redirect('/dashboard', user)
	else:
		context = {
			"Message" 	: 	"Invalid username or password",
			"Type"		:	"Error"
		}	
		return render(request, 'static/login.html', context)	

def logout_user(request):
	logout(request)
	context = {
		"Message" 	: 	"Welcome. Please login.",
		"Type"		:	"Default",
	}	
	return render(request, 'static/login.html', context)    

def register(request):
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']
	user = User.objects.filter(Q(username=username) | Q(email=email))
	
	if user.count() == 0:
		user = User.objects.create_user(username, email, password)
		user.save()
	
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('/dashboard', user)
	else:
		context = {
			"Message" 	: 	"username or email exist",
			"Type"		:	"Error"
		}	
		return render(request, 'static/login.html', context)