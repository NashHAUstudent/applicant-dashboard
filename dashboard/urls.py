# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.applicant_list, name='applicant_list'),

    path('applicant/<int:user_id>/', views.applicant_detail, name='applicant_detail'),

    path('applicant/<int:user_id>/delete/', views.applicant_delete, name='applicant_delete'),
]