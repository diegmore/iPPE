from django.shortcuts import render
from django.views.generic import  CreateView , ListView,DeleteView,UpdateView
from .models import Request_Type
from .forms import Request_Type_Form

from django.urls import reverse_lazy
# Create your views here.


class CreateRequest(CreateView):
    model = Request_Type
    form_class = Request_Type_Form
    template_name = "CreateRequest.html"
    success_url = reverse_lazy('requestType:listRequest')

class ListRequestTypes(ListView):
    model=Request_Type
    template_name="requiredList.html" 

class DeleteRequestType(DeleteView):
    model=Request_Type
    template_name='DeleteRequestType.html'
    success_url=reverse_lazy('requestType:listRequest')

class UpdateRequest(UpdateView):
    model=Request_Type
    form_class=Request_Type_Form
    template_name='CreateRequest.html'
    success_url=reverse_lazy('requestType:listRequest')