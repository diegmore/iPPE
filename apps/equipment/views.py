import json
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from datetime import date

from .models import Equipment, Work_Activities
from .forms import Equipment_Form
from apps.configurations.models import Element_Classification
# Create your views here.
class EquipmentCreate(CreateView):
    model = Equipment
    form_class = Equipment_Form
    template_name = 'equipment_form.html'

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['work_activities'] = []
        if "cancel" in request.POST:
            return redirect(reverse_lazy('equipment_config:equipment_list'))
        else:
            form = self.form_class(data)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                for wa in request.POST.getlist('work_activities'):
                    post.work_activities.add(wa)
                return redirect(reverse_lazy('equipment_config:equipment_list'))
            else:
                return redirect(reverse_lazy('equipment_config:equipment_list'))

class EquipmentList(ListView):
    model : Equipment
    template_name = 'equipment_list.html'

    def get_context_data(self, **kwargs):
        context = super(EquipmentList,self).get_context_data(**kwargs)
        context['element_classification'] = Element_Classification.objects.all 
        if not self.request.GET.get('filter'):
            context['filt'] = "All"
        else:
            context['filt'] = Element_Classification.objects.get(id = self.request.GET.get('filter'))
        return context

    def get_queryset(self):
        codpart = self.request.GET.get('filter')
        if not codpart:
            return Equipment.objects.order_by('id')
        else:
            return Equipment.objects.filter(element_classification=codpart).order_by('id')

class EquipmentDelete(View):     
    template_name = 'equipment_list.html'

    def post(self, request, *args, **kwargs):
        model = Equipment
        pk = request.POST['equipment_id']
        data = model.objects.get(id = pk)
        data.delete()
        return redirect(reverse_lazy('equipment_config:equipment_list'))

class EquipmentUpdate(UpdateView):
    model = Equipment
    form_class = Equipment_Form
    template_name = 'equipment_form.html'
    success_url = reverse_lazy('equipment_config:equipment_list')
