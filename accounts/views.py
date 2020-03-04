from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    #TODO NEEDS ROUTING TO HOMEPAGE
    return render(request,'accounts/signup.html')

def signup(request):
    return render(request,'accounts/signup.html')
