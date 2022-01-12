from django.shortcuts import render, redirect
from . import forms
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserModel as User

# Create your views here.


def home_view(request):
    return render(request, 'LoginApp/home.html')


def login_view(request):
    form = forms.LoginForm(request.POST)
    user = None
    if request.method == "POST":
        if form.is_valid():
            userid = form.cleaned_data['userid']
            password = form.cleaned_data['password']
            username = userid
            print('userid', userid)

            try:
                if '@' in userid:
                    username = User.objects.get(email=userid).username
                else:
                    username = User.objects.get(mobile=userid).username
            except:
                #print("except block")
                pass
            user = authenticate(username=username, password=password)
            print("avdhut", user)
            if user is not None:
                login(request, user)
                # print("avdhut")
                Users = User.objects.all()
                form = forms.LoginForm(request.POST)
                return render(request, 'LoginApp/user_details.html', {'Users': Users})

    return render(request, 'LoginApp/login.html', {'form': forms.LoginForm()})


def signup_view(request):
    next = request.GET.get('next')

    form = forms.RegistrationForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        confirm_password = form.cleaned_data.get('confirm password')
        mobile = form.cleaned_data.get('mobile')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)

        if next:
            return redirect(next)
        return redirect('/')

    return render(request, 'LoginApp/signup.html', {'form': form})

    return render(request, 'LoginApp/signup.html', {'form': forms.RegistrationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


def forgetpassword_view(request):
    return render(request, 'LoginApp/forgetpassword.html', {'form': forms.ForgetpasswordForm()})
