from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import logout,authenticate, login
from user.models import CustUser
from django.contrib.auth.models import User
# Create your views here.


def user_signup(request):
    if request.method =="POST":
        x = request.POST
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            user = User(username=first_name,email=email,password=password,first_name=first_name,last_name=last_name)
            user.save()
            user.set_password(password)
            user.save()
            user = CustUser(user=user,user_type="NO")
            user.save()
            user = authenticate(username=first_name, password=password)
            print(user)
            if user:
                login(request, user)
                print(request.user.get_full_name())
                return HttpResponseRedirect('/', )
        else:
            return render(request, "user/signup.html", {"message": "password don't match","x":x})
    else:
        context={}
        return render(request, "user/signup.html", context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def user_login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            print(request.user.get_full_name())
            return HttpResponseRedirect('/dashboard/', )
        else:
            return render(request, "user/login.html", {"message": "wrong credentials"})
    else:
        context = {}
        return render(request, "user/login.html", context)
