from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             messages.info(request, "invalid user")
#             return redirect('login')
#     return render(request, "login.html")
#
#
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['password1']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')
            # print("new user created")
        else:
            messages.info(request, "password is not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def commerce(request):
    return render(request, "bc.html")


def computer(request):
    return render(request, "bca.html")


def psychology(request):
    return render(request, "psy.html")


def physics(request):
    return render(request, "phy.html")


def chemistry(request):
    return render(request, "chem.html")
