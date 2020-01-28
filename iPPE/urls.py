"""iPPE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('config/', include('apps.configurations.urls', namespace='configurations')),
    path('config/', include('apps.body_configuration.urls', namespace='body_configurations')),
    # path('config/', include('apps.size_configuration.urls', namespace='size_configurations')),
    path('config/', include('apps.requestType.urls', namespace='RequestType')),
    path('config/', include('apps.size_configuration.urls', namespace='size_configurations')),
    path('config/', include('apps.equipment.urls', namespace='equipments_configurations')),
    path('config/', include('apps.warehouses.urls', namespace='warehouses_configurations')),
    
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns