import json
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from datetime import date
from django.db.models import Count
from django.core import serializers

from .models import Warehouse, Stockits
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
        return Warehouse.objects.order_by('id').annotate(warehouse_count=Count('stockits'))

    def get_context_data(self, **kwargs):
        context = super(WarehouseList, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['form'] = Warehouse_Form()
        context['id'] = pk
        context['stockists'] = Stockits.objects.all
        return context

class StockistsGrant(View):
    model = Warehouse
    second_model = Stockits
    
    def post(self, request, *args, **kwargs):
        pk_stock = request.POST.get('stockists')
        stock = Stockits.objects.get(pk = pk_stock)
        warehouse = Warehouse.objects.get(pk = request.POST.get('warehouse'))
        stock.warehouse = warehouse
        if 'None' in str(request.POST.get('ginput')):
            stock.grant_input = False
        else:
            stock.grant_input = True

        if 'None' in str(request.POST.get('goutput')):
            stock.grant_output = False
        else:
            stock.grant_output = True   
        stock.save()
        return redirect(reverse_lazy('warehouse_config:warehouses'))

class StockistList(View):

    def post(self, request, *args, **kwargs):
        id_warehouse = request.POST.get('id') 
        stockists = Stockits.objects.filter(warehouse=id_warehouse)
        print(stockists)
        data = serializers.serialize('json', stockists, fields=('name','position','grant_input','grant_output'))
        return HttpResponse(data, content_type='application/json')
    