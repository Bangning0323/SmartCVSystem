from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ForgetPswView

app_name = "authx"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/",    LoginView.as_view(),    name="login"),
    path("logout/",  LogoutView.as_view(),   name="logout"),
    path("forget/", ForgetPswView.as_view(), name="forget"),
]