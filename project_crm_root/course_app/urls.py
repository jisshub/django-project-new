from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.delete, name='delete'),
    path('edit/<int:new_id>', views.edit, name='edit'),
]
