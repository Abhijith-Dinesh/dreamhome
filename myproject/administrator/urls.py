from django.urls import path
from .views import *


urlpatterns = [
    path('rent/',rent,name='admin_rent'),
    path('manage/',managerent,name='admin_manage'),
    path('remove/<int:id>',deleterent,name='admin_deleterent'),
    path('edit/<int:id>',editrent,name='admin_editrent'),    
]