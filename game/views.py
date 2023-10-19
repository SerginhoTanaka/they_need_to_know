from django.shortcuts import render,redirect, get_object_or_404
from login.models import User, Score
from .models import FormUser
def play(request):
    return render(request, 'game/play.html')

def game(request):
    
    return render(request, 'game/game.html')

def user(request):

    return render(request, 'game/user.html')

def edit(request,user_id):
    user = get_object_or_404(User, pk=user_id)
    form = FormUser(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user.name = name
        user.email = email
        user.password = password
        user.save()
        return redirect('user')
    
    return render(request, 'game/edit.html', {'form': form, 'user': user})

def delete(request,user_id):
    get_object_or_404(User,pk=user_id)
    return render(request, 'game/delete.html')