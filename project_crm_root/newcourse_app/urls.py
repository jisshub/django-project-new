from django.urls import path
from . import views


# set a name for app
app_name = 'course_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('course/', views.course_add, name='course'),
    path('list/', views.list_course, name='list'),

]

