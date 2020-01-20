from django.conf.urls import url
from django.urls import path,include
from .views import EquipmentCreate, EquipmentList, EquipmentDelete, EquipmentUpdate

app_name = 'equipment_config'
urlpatterns = [
	path('equipment_list', EquipmentList.as_view(), name='equipment_list'),
    path('equipment_create', EquipmentCreate.as_view(), name='equipment_create'),
    path('equipment_update/<int:pk>/', EquipmentUpdate.as_view(), name='equipment_update'),
    path('equipment_delete', EquipmentDelete.as_view(), name='equipment_delete'),
]
