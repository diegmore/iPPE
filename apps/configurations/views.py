from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Element_Type, Element_Classification
from .forms import Element_Type_Form, Element_Classification_Form
# Create your views here.
class ClassificationList(ListView):
    model : Element_Classification
    template_name = 'element_type_list.html'
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
            return redirect(reverse_lazy('configurations:element_type_list'))        

class ClassificationForm(View):
    template_name = 'element_type_list.html'
    second_form_class = Element_Classification_Form

    def post(self, request, *args, **kwargs):
        form2=self.second_form_class(request.POST)
        if form2.is_valid():
            post = form2.save(commit=False)
            post.save()
            return redirect(reverse_lazy('configurations:element_type_list'))  

class ClassificationDelete(DeleteView):
    model = Element_Classification
    template_name = 'element_type_list.html'
    success_url = reverse_lazy('configurations:element_type_list')