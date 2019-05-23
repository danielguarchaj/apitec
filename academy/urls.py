from django.urls import path

from . import views

app_name = 'academy'

urlpatterns = [
    path('assignments_user/<int:user_id>/', views.AssignmentActivityList.as_view(), name='assignment_list'),
    path('assignments/<int:asgmt_id>/<int:user_id>/', views.AssignmentActivityRetrieveUpdate.as_view(), name='assignment_retrieve_update'),
]