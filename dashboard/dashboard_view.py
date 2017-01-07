from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import get_object_or_404
from .models import *
from datetime import datetime
from django.utils.dateformat import DateFormat
import json
import datetime
from django.http import JsonResponse


class getData(TemplateView):
	model = Dog
	template_name = "static/pages/dashboard.html"

	def post(self, request, *args, **kwargs):
		
		dogs_json = []
		date = request.POST.get('date')
		# search_key1 = request.POST.get('search_key1')
		# search_key2 = request.POST.get('search_key2')
		dog_list = Dog.objects.filter(start_date__lte=(date)).filter(end_date__gte=(date))
		for dog in dog_list:
			dogs_json.append({'first_name':dog.first_name, 'last_name':dog.last_name, 'end_date':dog.end_date.strftime('%Y-%m-%d'), 'start_date': dog.start_date.strftime('%Y-%m-%d')})
		return JsonResponse(dogs_json, safe=False)
  
class dashboardView(TemplateView):
	model = Dog
	template_name = "static/pages/dashboard.html"
	
	def post(self, request, *args, **kwargs):
		context = self.get_context_data()
		return super(TemplateView, self).render_to_response(context)

	def get_context_data(self, **kwargs):
		dog_data_list = []
		context = super(dashboardView, self).get_context_data(**kwargs)
		search_key1 = self.request.POST.get('search_key1', '')
		search_key2 = self.request.POST.get('search_key2', '')
		if (search_key1 != '' and search_key2 != ''):
			
			# dog_list = Dog.objects.filter(start_date__lte=(search_key1)).filter(end_date__gte=(search_key1))
			start = datetime.datetime.strptime(search_key1, "%Y-%m-%d")
			end = datetime.datetime.strptime(search_key2, "%Y-%m-%d")
			date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days+1)]
			for date in date_generated:
				dog_list = Dog.objects.filter(start_date__lte=(date.strftime("%Y-%m-%d"))).filter(end_date__gte=(date.strftime("%Y-%m-%d")))
				dog_data_list.append([date.strftime("%Y-%m-%d"), date.weekday(), len(dog_list)])
			
			context['first_week'] = range(0, dog_data_list[0][1])
			context['last_week'] = range(dog_data_list[len(dog_data_list)-1][1], 6)
			context['len_dog_data_list'] = range(0, len(dog_data_list)-1)
		# else:
		# 	dog_list = Dog.objects.filter(first_name__contains='')
		# context['dog_list'] = dog_list
		context['dog_data_list'] = dog_data_list
		context['search_key1'] = search_key1
		context['search_key2'] = search_key2
		return context

