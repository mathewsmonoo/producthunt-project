from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def login(request):
    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'Username or password is incorrect!'})

    return render(request,'accounts/login.html')

def logout(request):
    #LOGOUT SHOULD BE PUT AS A POST REQUEST
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def signup(request):
    if request.method=='POST':
        # The user has info and wants an account!
        if request.POST['password1'] == request.POST['password2']: # checking 'confirm password'
            try:
                user = User.objects.get(username=request.POST['username']) #Checks if username has been taken
                return render(request,'accounts/signup.html', {'error':'Username has already been taken'}) #Send back saying username already exists
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) #make new user
                auth.login(request, user) #log that user in
                return redirect('home') #redirect to home
        else:
            return render(request,'accounts/signup.html', {'error':'Passwords MUST match!'}) #Send back saying username already exists

    else:
        #User wants to enter info
        return render(request,'accounts/signup.html')
