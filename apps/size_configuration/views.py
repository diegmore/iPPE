import json
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from datetime import date

from .models import Size
from apps.body_configuration.models import BodyPart
from .forms import Size_Form
# Create your views here.
class SizeList(ListView):
    model : Size
    template_name = 'size_list.html'

    def get_context_data(self, **kwargs):
        context = super(SizeList,self).get_context_data(**kwargs)
        context['body_part'] = BodyPart.objects.all 
        if not self.request.GET.get('filter'):
            context['filt'] = "All"
        else:
            context['filt'] = BodyPart.objects.get(id = self.request.GET.get('filter'))
        return context
    
    def get_queryset(self):
        codpart = self.request.GET.get('filter')
        if not codpart:
            return Size.objects.order_by('id')
        else:
            return Size.objects.filter(body_area=codpart).order_by('id')

class SizeCreate(CreateView):
    model = Size
    form_class = Size_Form
    template_name = 'size_form.html'
    success_url = reverse_lazy('size_config:size_list')

class SizeUpdate(UpdateView):
    model = Size
    form_class = Size_Form
    template_name = 'size_form.html'
    success_url = reverse_lazy('size_config:size_list')

class SizeDelete(View):

    def post(self, request, *args, **kwargs):
        model = Size
        pk = request.POST['body_part_id']
        data = model.objects.get(id = pk)
        data.delete()
        return redirect(reverse_lazy('size_config:size_list'))

class SizeStatus(View):

    def post(self, request, pk):
        try:
            classification = Size.objects.get(id = pk)
            classification.status = bool(request.POST['status'] == 'true')
            classification.save()
            msg = "Success"
        except Exception as e:
            msg = '%s (%s)' % (e.message, type(e))
        return JsonResponse({'response':msg})
    