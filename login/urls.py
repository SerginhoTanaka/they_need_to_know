from django.urls import path
from . import views
from game import views 

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('play/', views.play, name='play'),  
]