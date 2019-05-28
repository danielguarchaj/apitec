from django.urls import path

from . import views

app_name = 'academy'

urlpatterns = [
    path('assignments/<int:user_pk>/<int:pk>/', views.AssignmentActivityRetrieve.as_view(), name='assignment_activity_retrieve'),
    path('deliveries/', views.AssignmentDeliveryCreate.as_view(), name='deliveries_create')
]