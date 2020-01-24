import json
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from datetime import date

from .models import BodyPart
from .forms import Body_Part_Form
# Create your views here.

class BodyPartList(ListView):
    model : BodyPart
    template_name = 'body_list.html'

    def get_queryset(self):
        return BodyPart.objects.order_by('id')
    
class BodyCreate(CreateView):
    model = BodyPart
    form_class = Body_Part_Form
    template_name = 'body_form.html'

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(reverse_lazy('body_config:body_part'))
        else:
            form = self.form_class(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect(reverse_lazy('body_config:body_part'))

class BodyStatus(View):

    def post(self, request, pk):
        try:
            classification = BodyPart.objects.get(id = pk)
            classification.status = bool(request.POST['status'] == 'true')
            classification.save()
            msg = "Success"
        except Exception as e:
            msg = '%s (%s)' % (e.message, type(e))
        return JsonResponse({'response':msg})

class BodyUpdate(UpdateView):    
    model = BodyPart
    form_class = Body_Part_Form   
    template_name = 'body_form.html'
    success_url = reverse_lazy('body_config:body_part')

class BodyDelete(View):     
    template_name = 'body_list.html'

    def post(self, request, *args, **kwargs):
        model = BodyPart
        print(request.POST)
        pk = request.POST['body_part_id']
        data = model.objects.get(id = pk)
        data.delete()
        return redirect(reverse_lazy('body_config:body_part'))