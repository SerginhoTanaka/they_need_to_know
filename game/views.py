from django.shortcuts import render,redirect, get_object_or_404
from django.templatetags.static import static
import random
import json 
from login.models import User, Score
from .models import FormUser
def play(request):
    return render(request, 'game/play.html')

def game(request):
    if request.method == 'POST':
        pass 
    url_qa = static('../../template/static/QA.json')

    with open(url_qa, 'r') as qa:
        data = json.load(qa)

    qa_keys = list(data.keys())
    random.shuffle(qa_keys)
    questions = [data[key] for key in qa_keys[:7]]  
    questions_data = [{'Pergunta': question['Pergunta'], 'Alternativas': question['Alternativas']} for question in questions]
    
    return render(request, 'game/game.html', {'questions': questions_data})

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