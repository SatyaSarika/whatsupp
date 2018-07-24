from django.views import View
from django.shortcuts import render,redirect

from messenger.forms import  *


from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

class SignupView(View):
    def get(self,request):
        signupform=SignupDETAILS()
        return render(request=request,template_name="signup.html",context={"form":signupform})
    def post(self,request):
        form=SignupDETAILS(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            user=authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect("messenger:msg")
            else:
                return redirect("messenger:sign_up")

class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('messenger:msg')
        loginform=LoginupDETAILS()
        return render(request=request,template_name="loginpage.html",context={"form":loginform})

    def post(self,request):
        form=LoginupDETAILS(request.POST)
        if form.is_valid():
            #user=User.objects.create_user(**form.cleaned_data)
            user=authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect("messenger:msg")
            else:
                return redirect("messenger:loginpage")

def logout_user(request):
    logout(request)
    return redirect("messenger:loginpage")