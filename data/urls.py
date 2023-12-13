from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_data),
    path('show/', views.get_all_data),
    path('find/<str:data_id>/', views.get_data_by_id),
    path('update/<str:data_id>/',views.update_person_by_id),
    path('delete/<str:data_id>/',views.delete_by_id)
]
