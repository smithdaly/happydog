from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import get_object_or_404
from .models import *

class VenuView(TemplateView):
	model = Venu
	template_name = "static/pages/venu_list.html"

	def post(self, request, *args, **kwargs):
		context = self.get_context_data()
		return super(TemplateView, self).render_to_response(context)

	def get_context_data(self, **kwargs):
		context = super(VenuView, self).get_context_data(**kwargs)
		search_key = self.request.POST.get('search_key', '')

		venu_list = Venu.objects.filter(venu_name__contains=search_key)
		context['venu_list'] = venu_list
		context['search_key'] = search_key
		return context

DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

class VenuUpdateView(TemplateView):
	model = Venu
	template_name = "static/pages/save_venu.html"

	def get(self, request, *args, **kwargs):
		context = self.get_context_data()
		return super(TemplateView, self).render_to_response(context)

	def post(self, request, *args, **kwargs):
		context = self.get_context_data()

		google_place_id = self.request.POST.get('google_place_id', '')
		venu_name = self.request.POST.get('venu_name', '')
		address = self.request.POST.get('address', '')
		phone = self.request.POST.get('phone', '')
		desc = self.request.POST.get('desc', '')
		trading_hours = self.request.POST.get('trading_hours', '')
		venu_id = self.request.POST.get('venu_id', '')

		if venu_id == '':
			venu = Venu(google_place_id=google_place_id, venu_name=venu_name, address=address, phone=phone, desc=desc, trading_hours=trading_hours)	
		else:
			venu = Venu.objects.get(id=venu_id)
			venu.google_place_id = google_place_id
			venu.venu_name = venu_name
			venu.address = address
			venu.phone = phone
			venu.desc = desc
			venu.trading_hours = trading_hours

		venu.save()
				
		context["message"] = "Save Successfully"
		context["venu"] = venu
	
		return super(TemplateView, self).render_to_response(context)

	def get_context_data(self, **kwargs):
		if self.request.method == 'POST':
			venu_id = self.request.POST.get('venu_id', '')
		else:
			venu_id = self.request.GET.get('venu_id', '')

		context = super(VenuUpdateView, self).get_context_data(**kwargs)
		if venu_id != '':
			venu = Venu.objects.get(id=venu_id)
			context["venu"] = venu

		context['days'] = DAYS
		context['months'] = range(1,24)

		return context

class VenuDeleteView(DeleteView):
	success_message = "Deleted Successfully"
	model = Venu
	success_url = '/dashboard/'

	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)