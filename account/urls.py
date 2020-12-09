from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = "account"
urlpatterns = [
    path("", views.edit, name="dashboard"),
    path("login/", auth_view.LoginView.as_view(), name="login"),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
]
