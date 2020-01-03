from django.shortcuts import render
from .models import Size, Body_Size
# Create your views here.
class SizeList(ListView):
    model : BodyPart
    template_name = 'body_list.html'
    form_class = Body_Part_Form

    def get_queryset(self):
        return BodyPart.objects.order_by('id')