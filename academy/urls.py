from django.urls import path

from . import views

app_name = 'academy'

urlpatterns = [
    path('assignments/', views.AssignmentActivityList.as_view(), name='assignment_list'),
]