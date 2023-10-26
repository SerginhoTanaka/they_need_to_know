from django.shortcuts import render, redirect, get_object_or_404
from django.templatetags.static import static
import random
import json
from django.contrib.auth.models import User
from login.models import Score
from .models import FormUser


def play(request):
    return render(request, 'game/play.html')


def game(request, user_id):
    url_qa = static('../../template/static/QA.json')
    with open(url_qa, 'r') as qa:
        data = json.load(qa)

    qa_keys = list(data.keys())
    random.shuffle(qa_keys)
    questions = [data[key] for key in qa_keys[:7]]
    correct_answers = [question['Resposta'] for question in questions]
    # print(correct_answers)
    # explanations = [question['Explicação'] for question in questions]
    questions_data = [{'Pergunta': question['Pergunta'],
                       'Alternativas': question['Alternativas']} for question in questions]

    if request.method == 'POST':
        answers = request.POST.getlist('resposta')

        for i, answer in enumerate(answers):
            if answer == correct_answers[i]:
                # explanation = explanations[i]
                user = get_object_or_404(User, pk=user_id)
                score = Score.objects.get(user=user)
                score.score += 10
                streak += 1
                if streak == 3:
                    score.score += 30
                score.save()
                return render(request, 'game/game.html', {'questions': questions_data, 'correct_answers': correct_answers})
            else:
                streak = 0

    return render(request, 'game/game.html', {'questions': questions_data})


def user(request):
    return render(request, 'game/user.html')


def edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    print(user_id, "id")
    if request.method == 'POST':
        form = FormUser(request.POST or None, instance=user)
        if form.is_valid():
            form.save()  
            return redirect('user')  
    else:
        form = FormUser(instance=user)
        
    return render(request, 'game/edit.html', {'form': form})

def delete(request, user_id):
    get_object_or_404(User, pk=user_id)
    return render(request, 'game/delete.html')
