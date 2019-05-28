from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', views.UserRetrieve.as_view(), name='user_retrieve'),
    path('assignments/<int:pk>/', views.UserGroupsRetrieve.as_view(), name='user_assignments')
]