from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
   path('',views.admin_login),
   path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
   path('admin_notesdata/',views.admin_notesdata,name='admin_notesdata'),
   path('admin_userdata/',views.admin_userdata,name='admin_userdata'),
]