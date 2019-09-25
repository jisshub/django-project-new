from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.course_list, name='course_list'),
    path('int:<course_id>', views.delete_course, name='delete'),
    path('int:<course2_id>', views.edit_course, name='edit'),
]
