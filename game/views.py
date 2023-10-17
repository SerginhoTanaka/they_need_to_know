from django.shortcuts import render

def play(request):
    return render(request, 'game/play.html')

def game(request):
    
    return render(request, 'game/game.html')