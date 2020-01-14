import json
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from datetime import date

from .models import Equipment, Work_Activities
from .forms import Equipment_Form

# Create your views here.
class EquipmentCreate(CreateView):
    model = Equipment
    form_class = Equipment_Form
    template_name = 'equipment_form.html'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if "cancel" in request.POST:
            return redirect(reverse_lazy('equipment_config:equipment_list'))
        else:
            form = self.form_class(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect(reverse_lazy('equipment_config:equipment_list'))
            else:
                return redirect(reverse_lazy('equipment_config:equipment_list'))
            print(form.errors)

class EquipmentList(ListView):
    model : Equipment
    template_name = 'equipment_list.html'

    def get_queryset(self):
        return Equipment.objects.order_by('id')