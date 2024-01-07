from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.loginUser,name='login'),
    path('signUp',views.signUp,name='signUp'),
    path('men',views.men,name='men'),
    path('women',views.women,name='women'),
    path('kids',views.kids,name='kids'),
    path('contact',views.contact,name='contact')

]