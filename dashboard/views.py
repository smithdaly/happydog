from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from pprint import pprint
from .models import *
from django.contrib.auth.models import User, Group, Permission
from django.db import OperationalError

@login_required(login_url='/')
def index(request):
	
	context = {}
	return render(request, 'static/pages/index_content.html', context)