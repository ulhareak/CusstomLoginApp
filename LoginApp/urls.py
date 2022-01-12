from . import views 
from django.urls import path 


app_name = 'LoginApp'

urlpatterns=[
    path('',views.home_view , name = 'home'),
    path('login/', views.login_view , name='login'),
    path('signup/',views.signup_view , name='signup'),
    path('forgetpassword/' , views.forgetpassword_view , name='forgetpassword' ) , 
    path('logout/' , views.logout_view , name = 'logout_user'),
]
