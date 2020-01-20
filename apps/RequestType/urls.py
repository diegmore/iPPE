from django.conf.urls import url
from django.urls import path,include
from .views import ShowList

app_name = 'requestType'
urlpatterns = [
	path('', ShowList.as_view(), name='ShowList'),
]
