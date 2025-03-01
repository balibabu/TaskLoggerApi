from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('id/<int:pk>', views.TaskGetUpdateDeleteView.as_view(), name='get-update-delete')
]