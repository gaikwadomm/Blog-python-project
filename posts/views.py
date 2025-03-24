from django.shortcuts import render, redirect
from .models import Posts
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    pos = Posts.objects.all()
    return render(request ,'index.html', {'posts': pos})

def posts(request, pk):
    pos = Posts.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': pos})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['code']
        password2 = request.POST['code2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'The Email is Already in use')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'The Username Already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'The Account Created Successfully')
                return redirect('login')
        
        else:
            messages.info(request, 'The Password not matching')
            return redirect('register')
    
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Credential Incorrect')
            return render(request, 'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def delete(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            # Delete the authenticated user
            user.delete()
            messages.info(request, 'Account Deleted Successfully')
            return redirect('/')
        else:
            # Show an error message if credentials are incorrect
            messages.info(request, 'Credentials Incorrect')
            return render(request, 'delete.html')
    else:
        # Render the delete form for GET request
        return render(request, 'delete.html')
