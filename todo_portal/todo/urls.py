from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskListView.as_view(), name = 'home'),
    path('task/<int:pk>', views.taskDetailView.as_view(), name = 'detail'),
    path('task/<int:pk>/edit', views.taskUpdateView.as_view(), name = 'edit'),
    path('task/<int:pk>/delete', views.taskDeleteView.as_view(), name = 'delete'),
]
