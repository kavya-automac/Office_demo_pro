from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('index',views.index, name='index'),
    path('all_emp',views.all_emp, name='all_emp'),
    path('add_emp',views.add_emp, name='add_emp'),
    path('remove_emp',views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>',views.remove_emp, name='remove_emp'),
    path('filter_emp',views.filter_emp, name='filter_emp'),
    path('logout',views.logout,name='logout'),

]
