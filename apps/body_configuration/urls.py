from django.conf.urls import url
from django.urls import path,include
from .views import BodyPartList, BodyCreate, BodyStatus, BodyUpdate, BodyDelete

app_name = 'body_config'
urlpatterns = [
	path('body_part', BodyPartList.as_view(), name='body_part'),
    path('body_create', BodyCreate.as_view(), name='body_create'),
    path('body_status/<int:pk>/', BodyStatus.as_view(), name='body_status'),
    path('body_update/<int:pk>/', BodyUpdate.as_view(), name='body_update'),
    path('body_delete', BodyDelete.as_view(), name='body_delete'),
]
