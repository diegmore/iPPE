from django.conf.urls import url
from django.urls import path,include
from .views import EquipmentCreate

app_name = 'equipment_config'
urlpatterns = [
	# path('body_part', BodyPartList.as_view(), name='body_part'),
    path('equipment_create', EquipmentCreate.as_view(), name='equipment_create'),
    # path('body_status/<int:pk>/', BodyStatus.as_view(), name='body_status'),
    # path('body_update/<int:pk>/', BodyUpdate.as_view(), name='body_update'),
    # path('body_delete', BodyDelete.as_view(), name='body_delete'),
]
