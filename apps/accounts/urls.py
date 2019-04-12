from django.urls import path
from apps.accounts.views import (
    UserListView, UserDeleteView, UserEditView, UserCreateView
)
from apps.accounts import views


urlpatterns = [
    path('', UserListView.as_view(), name='UserListView'),
    path('new/', UserCreateView.as_view(), name='UserCreateView'),
    path('save/', views.save, name='openduty.users.save'),
    path('testnotification/', views.testnotification, name='openduty.users.testnotification'),
    path('edit/<int:id>/', UserEditView.as_view(), name='UserEditView'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='UserDeleteView'),
]
