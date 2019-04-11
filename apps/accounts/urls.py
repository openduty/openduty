from django.conf.urls import url
from django.urls import path
from apps.accounts.views import UserListView, UserDeleteView
from apps.accounts import views


urlpatterns = [
    path('', UserListView.as_view(), name='UserListView'),
    path('new/', views.new, name='add_user'),
    path('save/', views.save, name='openduty.users.save'),
    path('testnotification/', views.testnotification, name='openduty.users.testnotification'),
    path('edit/<int:id>/', views.edit, name='edit_profile'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='UserDeleteView'),
]
