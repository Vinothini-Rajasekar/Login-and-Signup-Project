from django.shortcuts import render,redirect
from .form import CustomUserForm
from django.contrib.auth import authenticate,login


def signup(request):
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sign_in')

        else:
            print("error")
    return render(request,'sign_up.html')

def signin(request):
    print("admin")
    if request.method == 'POST' :
        print("admin1")
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        print(name)
        print(pwd)


        try:
            print(1)
            user=authenticate(request,username=name,password=pwd)
            print(2)
            print(user)
            if user is not None:
                print(3)
                print("admin5")
                login(request,user)
                print("admin6")
                return redirect('/welcome')

        except:
            pass
    return render(request,'sign_in.html')

def welcome(request):
    return render(request,'welcome.html')

  


# Create your views here.
