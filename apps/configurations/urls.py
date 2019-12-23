from django.conf.urls import url
from django.urls import path,include
from .views import ClassificationList, ClassificationForm, ClassificationDelete
app_name = 'config'
urlpatterns = [
	path('element_type', ClassificationList.as_view(), name='element_type_list'),
	path('element_classification', ClassificationForm.as_view(), name='element_classification_list'),
	path('delete_element_classification', ClassificationDelete.as_view(), name='element_classification_delete'),
]
