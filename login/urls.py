from django.urls import path
from . import views
from game.views import play

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgot/', views.forgot, name='forgot'),
    path('play', play, name='play'),

]