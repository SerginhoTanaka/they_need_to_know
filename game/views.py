from django.shortcuts import render,redirect, get_object_or_404
from django.templatetags.static import static
import random
import json 
from login.models import User, Score
from .models import FormUser
def play(request):
    return render(request, 'game/play.html')

def game(request,user_id):
    url_qa = '../../template/static/QA.json'  # Corrigi o caminho para o JSON

    with open(url_qa, 'r') as qa:
        data = json.load(qa)

    qa_keys = list(data.keys())
    random.shuffle(qa_keys)
    questions = [data[key] for key in qa_keys[:7]]  
    correct_answers = [question['Resposta'] for question in questions]
    explanations = [question['Explicação'] for question in questions]
    questions_data = [{'Pergunta': question['Pergunta'], 'Alternativas': question['Alternativas']} for question in questions]

    if request.method == 'POST':
        answers = request.POST.getlist('resposta')  

        for i, answer in enumerate(answers):
            if answer == correct_answers[i]:
                explanation = explanations[i]
                score = Score.objects.get(pk=user_id)
                score.score += 10
                streak += 1  
                if streak == 3:
                    score.score += 30
                score.save()
                return render(request, 'game/game.html', {'questions': questions_data, 'correct_answers': correct_answers, 'explanation': explanation})
            else:
                streak = 0
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