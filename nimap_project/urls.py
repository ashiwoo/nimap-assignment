from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list_create),
    path('clients/<int:pk>/', views.client_detail),
    path('clients/<int:client_id>/projects/', views.create_project),
    path('projects/', views.user_projects),
]
