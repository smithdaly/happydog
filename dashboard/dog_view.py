from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import get_object_or_404
from .models import *
from datetime import date
from django.utils.dateformat import DateFormat
from django.views.decorators.csrf import csrf_exempt
# from django.template import RequestContext

class dogView(TemplateView):
	model = Dog
	template_name = "static/pages/dog_list.html"

	def post(self, request, *args, **kwargs):
		context = self.get_context_data()
		return super(TemplateView, self).render_to_response(context)

	def get_context_data(self, **kwargs):
		context = super(dogView, self).get_context_data(**kwargs)
		search_key = self.request.POST.get('search_key', '')
		dog_list = Dog.objects.filter(first_name__contains=search_key) | Dog.objects.filter(last_name__contains=search_key)
		context['dog_list'] = dog_list
		context['search_key'] = search_key
		return context

DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

class dogUpdateView(TemplateView):
	model = Dog
	template_name = "static/pages/save_dog.html"

	def get(self, request, *args, **kwargs):
		context = self.get_context_data()
		return super(TemplateView, self).render_to_response(context)

	def post(self, request, *args, **kwargs):
		context = self.get_context_data()
		first_name = self.request.POST.get('first_name', '')
		last_name = self.request.POST.get('last_name', '')
		start_date = self.request.POST.get('start_date', '')
		end_date = self.request.POST.get('end_date', '')
		dog_id = self.request.POST.get('dog_id', '')
		if (first_name == '' or start_date == '' or end_date == ''):
			context["message"] = "Invailid!!!"
		else:
			if dog_id == '':
				dog = Dog(first_name=first_name, last_name=last_name, start_date=start_date, end_date=end_date)	
			else:
				dog = Dog.objects.get(id=dog_id)
				dog.first_name = first_name
				dog.last_name = last_name
				dog.start_date = start_date
				dog.end_date = end_date
				
			dog.save()
			context["message"] = "Save Successfully"
			context["dog"] = dog
	
		return super(TemplateView, self).render_to_response(context)

	def get_context_data(self, **kwargs):
		if self.request.method == 'POST':
			dog_id = self.request.POST.get('dog_id', '')
		else:
			dog_id = self.request.GET.get('dog_id', '')

		context = super(dogUpdateView, self).get_context_data(**kwargs)
		if dog_id != '':
			dog = Dog.objects.get(id=dog_id)
			context["dog"] = dog

		context['days'] = DAYS
		context['months'] = range(1,24)

		return context

class dogDeleteView(DeleteView):
	success_message = "Deleted Successfully"
	model = Dog
	success_url = '/dashboard/dog/'

	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)