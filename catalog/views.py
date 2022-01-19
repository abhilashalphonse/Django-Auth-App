from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'catalog/index.html')


def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        psw = request.POST['psw']
        psw2 = request.POST['psw2']

        myuser = User.objects.create_user(email, psw)
        myuser.fname = email[0:5]
        
        myuser.save()

        messages.success(request, "You are registered successfully")
        return redirect('signin')

    return render (request, 'catalog/signup.html')
def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        psw = request.POST['psw']

        user = authenticate(username=email , password=psw)
        if user is not None:
            login(request, user)
            fname = email
            return render(request, 'catalog/index.html', {'fname' : fname})


        else:
            messages.error( request, "User not exist")
            return redirect('index')




    return render(request, 'catalog/signin.html')


def signout(request):
    return render(request, 'catalog/signout.html')

    

