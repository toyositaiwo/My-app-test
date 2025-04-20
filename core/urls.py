from django.urls import path
from .views import ProcessMessageView, TaskStatusView

urlpatterns = [
    path('process/', ProcessMessageView.as_view(), name='process'),
    path('status/<str:task_id>/', TaskStatusView.as_view(), name='task_status'),
]
