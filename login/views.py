from django.shortcuts import render,redirect
from django.core.validators import validate_email,ValidationError
from django.contrib.auth.models import User 
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        return render(request, 'login/index.html')
    
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=email, password=password)
    if not user:
        return render(request, 'login/index.html', {'error': 'Invalid email or password'})
    else:
        auth.login(request, user)
        return render(request, 'game/play.html')
    
    
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password_confirmation')

        if not username or not password or not password2 or not email:
            return render(request, 'login/signup.html', {'error': 'Please fill all the fields'})
        
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'login/signup.html', {'error': 'Please enter a valid email'})

        if password != password2:
            return render(request, 'login/signup.html', {'error': 'Passwords do not match'})
        
        if len(password) < 6:
            return render(request, 'login/signup.html', {'error': 'Password must be at least 6 characters'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'login/signup.html', {'error': 'Username already taken'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'login/signup.html', {'error': 'Email already taken'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('login')
    
    return render(request, 'login/signup.html')






