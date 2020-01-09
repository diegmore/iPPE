from django.conf.urls import url
from django.urls import path,include
from .views import SizeList, SizeCreate, SizeUpdate, SizeDelete, SizeStatus

app_name = 'size_config'

urlpatterns = [
    path('size_list', SizeList.as_view(), name='size_list'),
    path('size_create', SizeCreate.as_view(), name='size_create'),
    path('size_update/<int:pk>/', SizeUpdate.as_view(), name='size_update'),
    path('size_delete', SizeDelete.as_view(), name='size_delete'),
    path('size_status/<int:pk>/', SizeStatus.as_view(), name='size_status'),
]
