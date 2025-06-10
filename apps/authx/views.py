from django.http import HttpResponse
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import User

# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, "authx/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(name=username)

        except Exception as e:
            print(e)
            return HttpResponse("Username not found")

        # 如果用户名对，就判断密码有没有输入正确
        if password != user.password:
            return HttpResponse("Password Error")

        return redirect("authx:redirect")



class RegisterView(View):
    def get(self, request):
        return render(request, "authx/register.html")

    def post(self, request):
        name = request.POST.get("username")
        passwd = request.POST.get("password")

        user = User.objects.all()
        for i in user:
            if name == i.username:
                return HttpResponse("Username already exists")
        try:
            User.objects.create(name=name, password=passwd)
        except Exception as e:
            return HttpResponse("Register error")

        return redirect("authx:login")


class LogoutView(LoginRequiredMixin, View):
    """
    Logs out on GET and redirects to the login page.
    """

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("authx:login")


class ForgetView(View):
    def get(self, request):
        return render(request, "authx/password-reset.html")


class AccountView(View):
    def get(self, request):
        return render(request, "profile/detailView.html")


class SearchView(View):
    def get(self, request):
        return render(request, "resumes/search.html")
