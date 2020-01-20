from django.conf.urls import url
from django.urls import path,include
from .views import WarehouseCreate, WarehouseList

app_name = 'warehouse_config'
urlpatterns = [
	path('warehouses', WarehouseList.as_view(), name='warehouses'),
    path('warehouse_create', WarehouseCreate.as_view(), name='warehouse_create'),
    # path('body_status/<int:pk>/', BodyStatus.as_view(), name='body_status'),
    # path('body_update/<int:pk>/', BodyUpdate.as_view(), name='body_update'),
    # path('body_delete', BodyDelete.as_view(), name='body_delete'),
]
