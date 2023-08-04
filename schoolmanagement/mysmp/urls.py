from django.contrib import admin
from django.urls import path,include
from.import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('list/',views.stud_list,name='stud_list'),
    path('create/',views.stud_create,name='stud_create'),
    path('update/<int:pk>', views.stud_update, name='stud_update'),
    path('delete/<int:pk>', views.stud_delete, name='stud_delete'),
    path('register/',views.register, name='register'),
    path('',auth_views.LoginView.as_view(template_name='login.html'), name='login'),      
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),     
]