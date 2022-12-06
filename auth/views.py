from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

# Create your views here.
def home(request):
    return render(request, "auth/index.html")

def signup(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mob= request.POST.get('mob')
        dep= request.POST.get('dep')
        html=request.POST.get('html')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! please try some other username")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "usernamen must be unser 10 characters")
        
        if pass1 != pass2:
            messages.error(request, "passwords didn't match")
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha_Numeric!")
            return redirect('home')
        
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname    
        
        myuser.save()
        
        messages.success(request,"Your Account has been created Successfully.")
        return redirect('signin')
    
    return render(request,"auth/signup.html")

def signin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request,"auth/leave.html",{'fname':fname})
          
        
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
        
    return render(request,"auth/signin.html")
   

def signout(request):
   logout(request)
   messages.success(request,"logged out successfully")
   return redirect('home')

def leave(request):
    text=request.POST.get('text')
    return render(request,"auth/signin.html")
    