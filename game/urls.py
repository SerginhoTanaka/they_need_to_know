from django.urls import path
from . import views

urlpatterns = [
    path('play/',views.play, name = "play"),
    path('game/',views.game, name = "game"),
    path('user/',views.user, name = "user"),
    path('edit/<int:user_id>',views.edit, name = "edit"),
    path('delete/<int:user_id>',views.delete, name = "delete"),
]