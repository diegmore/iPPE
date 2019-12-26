from django.conf.urls import url
from django.urls import path,include
from .views import ClassificationList, ClassificationForm, ClassificationDelete, ClassificationUpdate, UpdateStatus
app_name = 'config'
urlpatterns = [
	path('element_type', ClassificationList.as_view(), name='element_type_list'),
	path('element_classification', ClassificationForm.as_view(), name='element_classification_list'),
	path('delete_element_classification', ClassificationDelete.as_view(), name='delete_element_classification'),
	path('update/<int:pk>/', ClassificationUpdate.as_view(), name='update_element_classification'),
	path('updatestatus/<int:pk>/', UpdateStatus.as_view(), name='update_status'),
]
