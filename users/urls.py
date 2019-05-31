from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', views.UserRetrieveUpdate.as_view(), name='user_retrieve_update'),
    path('student/<int:pk>/', views.StudentUpdate.as_view(), name='student_update'),
    path('assignments/<int:pk>/', views.UserGroupsRetrieve.as_view(), name='user_assignments')
]