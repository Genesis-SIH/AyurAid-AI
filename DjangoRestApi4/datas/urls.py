from django.urls import path
from datas import views 
 
urlpatterns = [ 
    path(r'^api/datas$', views.data_list),
    path(r'^api/datas/(?P<pk>[0-9]+)$', views.data_detail),
    path(r'^api/datas/published$', views.data_list_published)
]