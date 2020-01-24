from django.conf.urls import url
from django.urls import path,include
from .views import WarehouseCreate, WarehouseList, StockistsGrant, StockistList

app_name = 'warehouse_config'
urlpatterns = [
	path('warehouses', WarehouseList.as_view(), name='warehouses'),
    path('warehouse_create', WarehouseCreate.as_view(), name='warehouse_create'),
    path('stockists', StockistsGrant.as_view(), name='stockists'),
    path('stockist_list/<int:pk>/', StockistList.as_view(), name='stockist_list'),
    # path('body_update/<int:pk>/', BodyUpdate.as_view(), name='body_update'),
    # path('body_delete', BodyDelete.as_view(), name='body_delete'),
]
