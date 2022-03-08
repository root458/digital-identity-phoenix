from django.contrib.auth import views as auth_views
from django.urls import path
from . import views as v

urlpatterns = [
    path('login/', view=auth_views.LoginView.as_view(), name='login'),
]