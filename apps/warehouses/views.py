import json
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from datetime import date

from .models import Warehouse
from .forms import Warehouse_Form
# Create your views here.
    
class WarehouseCreate(CreateView):
    model = Warehouse
    form_class = Warehouse_Form
    template_name = 'warehouses_form.html'

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(reverse_lazy('warehouse_config:warehouses'))
        else:
            form = self.form_class(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect(reverse_lazy('warehouse_config:warehouses'))

class WarehouseList(ListView):
    model : Warehouse
    template_name = 'warehouses_list.html'

    def get_queryset(self):
        return Warehouse.objects.order_by('id')