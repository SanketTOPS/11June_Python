from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
   path('',views.admin_login),
   path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
   path('admin_notesdata/',views.admin_notesdata,name='admin_notesdata'),
   path('admin_userdata/',views.admin_userdata,name='admin_userdata'),
   path('notes_approve/<int:id>',views.notes_approve,name='notes_approve'),
   path('notes_reject/<int:id>',views.notes_reject,name='notes_reject'),
]