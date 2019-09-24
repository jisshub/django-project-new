from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.course_list, name='course_list'),
]
