from django.urls import path
from . import views

urlpatterns = [
    path('users', views.UsersView.as_view()),
    path('users/<int:pk>/updatedelete/', views.UsersUpdateDeleate.as_view(), name='user-deleteupdate'),
    path('login/', views.LoginView.as_view(), name='user-login'),
]