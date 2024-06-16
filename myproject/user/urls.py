from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='user_index'),
    path('signin/',signin,name='user_signin'),
    path('signup/',signup,name='user_signup'),
    path('logout/',logout,name='user_logout'),
   
    path('plan/',plan,name='user_plan'),
    path('choose/',choose,name='user_choose'),
     path('profile/',profile,name='user_profile'),
    # path('create/',create_product,name='user_create_product'),
    
]