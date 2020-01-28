from django.conf.urls import url
from django.urls import path,include
from .views import CreateRequest,ListRequestTypes, DeleteRequestType,UpdateRequest

app_name = 'requestType'

urlpatterns = [
	path('CreateRequest', CreateRequest.as_view(), name='CreateRequest'),
	path('listRequest', ListRequestTypes.as_view(), name='listRequest'),
	path('DeleteRequest/<int:pk>/', DeleteRequestType.as_view(), name='DeleteRequest'),
	path('UpdateRequest/<int:pk>/', UpdateRequest.as_view(), name='UpdateRequest'),
]
