from django.contrib import admin
from django.urls import path
from em_web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dep_list/', views.dep_list),
    path('dep_add/', views.dep_add),
    path('dep_del/', views.dep_del),
    path('dep_update/', views.dep_update),
    path('emp_list/', views.emp_list),
    path('emp_add/', views.emp_add),
    path('emp_del/', views.emp_del)
]
