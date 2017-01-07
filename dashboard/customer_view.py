from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import get_object_or_404
from .models import *

class CustomerView(TemplateView):
	model = Customer
	template_name = "static/pages/customer_list.html"

	def post(self, request, *args, **kwargs):
		context = self.get_context_data()
		return super(TemplateView, self).render_to_response(context)

	def get_context_data(self, **kwargs):
		context = super(CustomerView, self).get_context_data(**kwargs)
		search_key = self.request.POST.get('search_key', '')

		customer_list = Customer.objects.filter(customer_name__contains=search_key)
		context['customer_list'] = customer_list
		context['search_key'] = search_key
		# context = []
		return context

DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

class CustomerUpdateView(TemplateView):
	model = Customer
	template_name = "static/pages/save_customer.html"

	def get(self, request, *args, **kwargs):
		context = self.get_context_data()
		return super(TemplateView, self).render_to_response(context)

	def post(self, request, *args, **kwargs):
		context = self.get_context_data()

		# google_place_id = self.request.POST.get('google_place_id', '')
		customer_name = self.request.POST.get('customer_name', '')
		address = self.request.POST.get('address', '')
		phone = self.request.POST.get('phone', '')
		desc = self.request.POST.get('desc', '')
		
		customer_id = self.request.POST.get('customer_id', '')

		if customer_id == '':
			customer = Customer(customer_name=customer_name, address=address, phone=phone, desc=desc, create_date=date.today())	
		else:
			customer = Customer.objects.get(id=customer_id)
			customer.customer_name = customer_name
			customer.address = address
			customer.phone = phone
			customer.desc = desc
			customer.create_date = date.today()

		customer.save()
				
		context["message"] = "Save Successfully"
		context["customer"] = customer
	
		return super(TemplateView, self).render_to_response(context)

	def get_context_data(self, **kwargs):
		if self.request.method == 'POST':
			customer_id = self.request.POST.get('customer_id', '')
		else:
			customer_id = self.request.GET.get('customer_id', '')

		context = super(CustomerUpdateView, self).get_context_data(**kwargs)
		if customer_id != '':
			customer = Customer.objects.get(id=customer_id)
			context["customer"] = customer

		context['days'] = DAYS
		context['months'] = range(1,24)

		return context

class CustomerDeleteView(DeleteView):
	success_message = "Deleted Successfully"
	model = Customer
	success_url = '/dashboard/customer/'

	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)