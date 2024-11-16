from django.urls import path
from  . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/new/', views.task_create, name='task_create'),
    path('<int:task_id>/edit/', views.task_update, name='task_update'),
    path('<int:task_id>/delete/', views.task_delete, name='task_delete')
]



