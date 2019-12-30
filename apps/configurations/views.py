import json
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from datetime import date

from .models import Element_Type, Element_Classification
from .forms import Element_Type_Form, Element_Classification_Form

# Create your views here.
class ClassificationList(ListView):
    model : Element_Classification
    template_name = 'element_classification_list.html'
    form_class = Element_Type_Form
    second_form_class = Element_Classification_Form

    def get_queryset(self):
        return Element_Classification.objects.order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super(ClassificationList, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['form'] = Element_Type_Form()
        context['form2'] = Element_Classification_Form()
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(reverse_lazy('configurations:element_classification'))        

class ClassificationForm(View):
    template_name = 'element_type_list.html'
    second_form_class = Element_Classification_Form

    def post(self, request, *args, **kwargs):
        form2 = self.second_form_class(request.POST)
        if form2.is_valid():
            post = form2.save(commit=False)
            post.save()
            return redirect(reverse_lazy('configurations:element_classification'))  

class ClassificationDelete(View):     
    template_name = 'element_type_list.html'

    def post(self, request, *args, **kwargs):
        model = Element_Classification
        pk = request.POST['element_type_id']
        data = model.objects.get(id = pk)
        data.delete()
        return redirect(reverse_lazy('configurations:element_classification'))

class ClassificationUpdate(UpdateView):    
    model = Element_Classification
    form_class = Element_Classification_Form    
    template_name = 'element_form.html'
    success_url = reverse_lazy('configurations:element_classification')

class UpdateStatus(View):
    def post(self, request, pk):
        try:
            classification = Element_Classification.objects.get(id = pk)
            classification.status = bool(request.POST['status'] == 'true')
            classification.save()
            msg = "Success"
        except Exception as e:
            msg = '%s (%s)' % (e.message, type(e))
        return JsonResponse({'response':msg})

class TypeList(ListView):
    model : Element_Type
    template_name = 'type_list.html'
    form_class = Element_Type_Form

    def get_queryset(self):
        return Element_Type.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(TypeList, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['form'] = Element_Type_Form()
        context['id'] = pk
        return context
    
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(reverse_lazy('configurations:type_list'))

class TypeDelete(View):     
    template_name = 'element_type_list.html'

    def post(self, request, *args, **kwargs):
        model = Element_Type
        pk = request.POST['element_type_id']
        data = model.objects.get(id = pk)
        data.delete()
        return redirect(reverse_lazy('configurations:type_list'))

class TypeUpdate(UpdateView):    
    model = Element_Type
    form_class = Element_Type_Form    
    template_name = 'type_edit.html'
    success_url = reverse_lazy('configurations:type_list')

def SimpleView(request):
    return render(request,'base1.html')